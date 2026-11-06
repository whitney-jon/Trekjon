"""Vertical (1080x1920) bar chart race in the channel's reference style.
(Working copy of graph-race/goals_race_vertical.py from the Project, with unused sport textures/icons trimmed,
the trophy legend made generic ("Cup") and Scottish/European club colours added.)
House rules: safe zones (top 150, bottom 1650, 50px sides), Plus Jakarta Sans SemiBold only.
"""
import glob
import os
import subprocess
import sys

import matplotlib

matplotlib.use("Agg")
import numpy as np
import pandas as pd
from matplotlib import font_manager as fm
from matplotlib import patheffects
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle, RegularPolygon
from PIL import Image, ImageFilter

W, H, FPS = 1080, 1920, 30

SAFE_TOP, SAFE_BOTTOM, SAFE_X = 150, 1650, 50
RIGHT_LIMIT = W - SAFE_X
GHOST_ALPHA = 0.2

HEADER_H = 380
TOP_N = 9
ROW_H, BAR_H = 118, 94
Y0 = 440
ROW0_YC = Y0 + ROW_H / 2
LAST_YC = ROW0_YC + (TOP_N - 1) * ROW_H
GHOST_YC = 1730
BAR_X0 = 440
BAR_MAX_W = 480
LEAD_W0 = 400
PILL_H, PILL_GAP, PILL_PAD = 62, 10, 18
CHIP_W, CHIP_H, CHIP_INSET = 68, 40, 14
YEAR_X, YEAR_Y = BAR_X0 + BAR_MAX_W // 2, 1568
ICON_R, ICON_GAP = 64, 40
WIDE_LOGO_H = 60

TITLE_PX, NAME_PX, VALUE_PX, CHIP_PX, YEAR_PX = 72, 36, 52, 27, 98
EVENT_SECONDS, EVENT_FADE = float(os.environ.get("EVENT_SECONDS", 3.2)), 8
VALUE_GAP = 16
LOGO_R = 36
MVP_H, MVP_PX, MVP_GAP = 64, 40, 12


def soft_shadow(color="#000000", strength=1.0):
    return [patheffects.SimplePatchShadow(offset=(0, -4.5), shadow_rgbFace=color, alpha=min(1, 0.14 * strength)),
            patheffects.SimplePatchShadow(offset=(0, -2.5), shadow_rgbFace=color, alpha=min(1, 0.22 * strength)),
            patheffects.SimplePatchShadow(offset=(0, -1.2), shadow_rgbFace=color, alpha=min(1, 0.30 * strength)),
            patheffects.Normal()]

FRAMES_PER_YEAR = 36
SEASON_LABELS = False
FRAMES_LAST = 24
HOLD_START, HOLD_END = 30, 100

DARK_TXT = dict(text="#f4f6fb", shadow="#000000", shadow_a=1.3)
LIGHT_TXT = dict(text="#16162a", shadow="#1a1a2e", shadow_a=0.55)
THEMES = {
    "football": dict(kw=["goal", "football", "soccer", "champions", "fifa", "scorer", "league", "striker", "trophies"],
                     icon="ball", dark=True, texture="stripes",
                     bg_top="#0b1033", bg_bot="#1e0f4e", glow="#26226e", hdr_l="#4c1d95", hdr_r="#1e4096",
                     rule="#f5c542", accent="#ff5d8f", title="#ffffff", pill_bg="#f4f6fb", pill_fg="#10153a",
                     chip="#0b1033", palette=["#ff3d6e", "#4c8dff", "#ffc83d", "#3dd68c", "#8e7cff", "#2bc0b4", "#ff922b", "#e599f7"], **DARK_TXT),
}
DEFAULT_THEME = "football"


def pick_theme(topic):
    return DEFAULT_THEME


COUNTRY_COLORS = {
    "BR": "#F7E733", "GB": "#2D4BFF", "PT": "#FF3D6E", "AR": "#74C7FF", "DE": "#FAB005", "US": "#3C78FF",
    "FR": "#2F5DFF", "ES": "#E63946", "IT": "#4DA3FF", "NL": "#FF7A1A", "RU": "#E5262D", "TR": "#E30A17",
    "RO": "#F9D71C", "CH": "#E8303A", "UA": "#FFD500",
    "GB-ENG": "#EDEFF7", "GB-SCT": "#1F5FBF", "GB-WLS": "#D30731", "GB-NIR": "#2FA84F",
}


def parse_codes(raw):
    out = []
    for k, part in enumerate(p for p in raw.split("|") if p):
        code, _, yr = part.partition(":")
        out.append((float("-inf") if k == 0 or not yr else int(yr), code.strip().upper()))
    return sorted(out, key=lambda t: t[0])


def code_at(timeline, year):
    cur = timeline[0][1] if timeline else ""
    for start, code in timeline:
        if year >= start:
            cur = code
    return cur


def px(size):
    return size * 0.72


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rel_lum(c):
    lin = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a, b):
    la, lb = rel_lum(a), rel_lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def ensure_contrast(col, bg, target=3.0):
    target_end = (1, 1, 1) if rel_lum(bg) < 0.4 else (0, 0, 0)
    c = col
    for k in range(1, 21):
        if contrast(c, bg) >= target:
            break
        c = tuple(col[i] + (target_end[i] - col[i]) * k * 0.05 for i in range(3))
    return c


def find_font(cli_path=None):
    cands = [cli_path] if cli_path else []
    for root in ("/home/claude/gr", "/home/claude/fonts", "/mnt/user-data/uploads", "/usr/share/fonts", "."):
        cands += glob.glob(f"{root}/**/PlusJakartaSans*SemiBold*.ttf", recursive=True)
    for c in cands:
        if c and os.path.exists(c):
            return c
    sys.exit("Plus Jakarta Sans SemiBold .ttf not found - pass --font /path/to/PlusJakartaSans-SemiBold.ttf")


QUESTION = {"text": None}
MVP = {}
MVP_ICON = {"img": None}
RECORD = {"L": None, "T": None, "rows": None}
REC_SUB = 0.56
TROPHY = {}
TROPHY_ICONS = {}
TROPHY_H, TROPHY_GAP = 58, 10
TROPHY_SHOW = 26
VALS_AT = {}
GROUP_SHOW = 60
LAST_YEAR = {"y": None}
LEGEND_Y = 418
TROPHY_FILES = {"L": ["league"], "F": ["fa-cup"], "C": ["league-cup"], "S": ["community-shield"],
                "E": ["european-cup"], "U": ["uefa-cup", "european-cup"], "K": ["uefa-cup", "european-cup"],
                "W": ["uefa-cup", "european-cup"], "O": ["uefa-cup", "european-cup"],
                "P": ["super-cup", "european-cup"], "I": ["club-world-cup", "super-cup", "european-cup"],
                "G": ["golden-boot"], "B": ["ballon-dor"]}
TROPHY_LEGEND = [("L", "League"), ("F", os.environ.get("CUP_LABEL", "FA Cup")), ("C", "League Cup"), ("S", os.environ.get("SHIELD_LABEL", "Shield")),
                 ("E", os.environ.get("EUROPE_LABEL", "Europe")), ("U", "Europa"), ("I", "World"), ("G", "Golden Boot"), ("B", "Ballon d'Or")]
TROPHY_MODE = {"group": False}
STARS = {}
RANK_N = {"n": None}
SNAP = {"on": False, "lab": None}
YEAR_FLAGS = {}
FLAG_DIR = {"d": None}
SQUARE_FLAGS = {"ch", "va", "CH", "VA"}
VALFMT = {"on": False, "pre": "", "suf": "", "bn": False}


def fmt_val(x):
    if VALFMT.get("off") and x > 0.01:
        x = x + VALFMT["off"]
    if VALFMT["bn"] and x >= 999.5:
        return f"{VALFMT['pre']}{x / 1000:.{1 if x >= 9999.5 else 2}f}bn"
    return f"{VALFMT['pre']}{x:,.{VALFMT.get('dec', 0)}f}{VALFMT['suf']}"
STAR_R, STAR_DX = 15, 33
TXT_W = {}
NAME_TL = {}
SPLIT = {"vals": None, "labels": None, "colors": None}
LOGO_TL = {}
COLOR_TL = {}
YEAR_LABELS = {}


def load(path):
    topic, events, skip = None, [], 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("#"):
                break
            skip += 1
            body = line.lstrip("# ").strip()
            if body.lower().startswith("topic:"):
                topic = body[6:].strip()
            elif body.lower().startswith("label-flag:"):
                k_, v_ = [x.strip() for x in body[11:].split("|", 1)]
                YEAR_FLAGS[int(k_)] = v_.lower()
            elif body.lower().startswith("label:"):
                k_, v_ = [x.strip() for x in body[6:].split("|", 1)]
                YEAR_LABELS[int(k_)] = v_
            elif body.lower().startswith("color:"):
                parts_ = [x.strip() for x in body[6:].split("|")]
                tl_ = []
                for seg_ in parts_[1:]:
                    y_, spec_ = seg_.split(":", 1)
                    fc_, _, ec_ = spec_.partition("/")
                    tl_.append((int(y_), fc_.strip(), ec_.strip() or None))
                COLOR_TL[parts_[0]] = sorted(tl_)
            elif body.lower().startswith("logo:"):
                parts_ = [x.strip() for x in body[5:].split("|")]
                LOGO_TL[parts_[0]] = sorted((int(sg.split(":", 1)[0]), sg.split(":", 1)[1].strip()) for sg in parts_[1:])
            elif body.lower().startswith("trophy:"):
                parts_ = [x.strip() for x in body[7:].split("|")]
                TROPHY[parts_[0]] = {int(sg.split(":", 1)[0]): sg.split(":", 1)[1].strip() for sg in parts_[1:]}
            elif body.lower().startswith("trophy-mode:"):
                TROPHY_MODE["group"] = body[12:].strip().lower() == "group"
            elif body.lower().startswith("snap-labels"):
                SNAP["on"] = True
            elif body.lower().startswith("question:"):
                QUESTION["text"] = body[9:].strip()
            elif body.lower().startswith("event:"):
                parts = [x.strip() for x in body[6:].split("|")]
                events.append(dict(year=int(parts[0]), text=parts[1], who=parts[2] if len(parts) > 2 else None))
    df = pd.read_csv(path, skiprows=skip)
    cols = list(df.columns[1:])
    names, codes = [], []
    for c in cols:
        n, sep, cc = c.rpartition(" #")
        if not sep:
            n, cc = c, ""
        if "|" in n:
            parts = n.split("|")
            tl = [(None, parts[0].strip())] + [(int(x.rsplit(":", 1)[1]), x.rsplit(":", 1)[0].strip()) for x in parts[1:]]
            n = tl[-1][1]
            NAME_TL[n] = tl
        names.append(n)
        codes.append(cc.upper())
    vals = df[cols].to_numpy(float)
    years = df[df.columns[0]].to_numpy(int)
    return topic, names, codes, years, vals, events


def ranks_of(v):
    order = sorted(range(len(v)), key=lambda i: (-v[i], i))
    r = np.empty(len(v))
    for pos, i in enumerate(order):
        r[i] = pos
    return r


def smooth(t):
    return t * t * (3 - 2 * t)


def stable_ranks(vals):
    out, prev = [], None
    for v in vals:
        if prev is None:
            r = ranks_of(v)
        else:
            order = sorted(range(len(v)), key=lambda i: (-v[i], prev[i]))
            r = np.empty(len(v))
            for pos, i in enumerate(order):
                r[i] = pos
        if RANK_N["n"]:
            r = np.where(np.asarray(v) <= 0, np.minimum(r, TOP_N), r)
        out.append(r)
        prev = r
    return out


def build_timeline(years, vals):
    key_ranks = stable_ranks(vals)
    frames = [(years[0], vals[0], key_ranks[0], None, None)] * HOLD_START
    for k in range(len(vals) - 1):
        n = FRAMES_LAST if k == len(vals) - 2 else FRAMES_PER_YEAR
        for f in range(1, n + 1):
            t = f / n
            v = vals[k] + (vals[k + 1] - vals[k]) * t
            r = key_ranks[k] + (key_ranks[k + 1] - key_ranks[k]) * smooth(t)
            frames.append((years[k + 1] if (t >= 0.5 or SEASON_LABELS) else years[k], v, r, None, None))
    frames += [(years[-1], vals[-1], key_ranks[-1], None, None)] * HOLD_END
    return frames


def build_timeline_paced(years, vals, total_frames, hold_end):
    key_ranks = stable_ranks(vals)
    n_tr = len(vals) - 1
    interest = np.zeros(n_tr)
    for k in range(n_tr):
        r0, r1 = key_ranks[k], key_ranks[k + 1]
        near = (np.minimum(r0, r1) <= TOP_N + 1)
        interest[k] = np.minimum(np.abs(r1 - r0), 3)[near].sum()
        if np.argmax(vals[k]) != np.argmax(vals[k + 1]):
            interest[k] += 4
        top = np.argsort(-vals[k + 1])[:TOP_N]
        grow = (vals[k + 1][top] - vals[k][top]).clip(0).sum() / max(vals[k + 1].max(), 1)
        interest[k] += min(grow * 6, 2)
    w = 0.8 + interest
    budget = total_frames - hold_end
    lo, hi = int(os.environ.get("PACE_LO", 10)), int(os.environ.get("PACE_HI", 90))
    f = np.full(n_tr, budget / n_tr)
    for _ in range(30):
        f = np.clip(w * budget / w.sum(), lo, hi)
        free = ~((f == lo) | (f == hi))
        if not free.any():
            break
        spare = budget - f[~free].sum()
        w2 = w.copy(); w2[~free] = 0
        f[free] = np.clip(w2[free] * spare / max(w2[free].sum(), 1e-9), lo, hi)
        if abs(f.sum() - budget) < 1:
            break
    f = np.maximum(np.round(f).astype(int), lo)
    frames = []
    for k in range(n_tr):
        n = int(f[k])
        for j in range(1, n + 1):
            t = j / n
            v = vals[k] + (vals[k + 1] - vals[k]) * t
            r = key_ranks[k] + (key_ranks[k + 1] - key_ranks[k]) * smooth(t)
            frames.append((years[k + 1] if (t >= 0.5 or SEASON_LABELS) else years[k], v, r, None))
    frames = [(years[0], vals[0], key_ranks[0], None)] + frames
    frames += [(years[-1], vals[-1], key_ranks[-1], None)] * hold_end
    return frames


def ypos(pos):
    n = TOP_N
    if pos <= n - 1:
        return ROW0_YC + pos * ROW_H
    if pos <= n:
        return LAST_YC + (pos - (n - 1)) * (GHOST_YC - LAST_YC)
    return GHOST_YC + (pos - n) * ROW_H


def row_alpha(pos):
    n = TOP_N
    if pos <= n - 1:
        return 1.0
    if pos <= n - 0.7:
        return 1.0 - (pos - (n - 1)) / 0.3 * (1.0 - GHOST_ALPHA)
    if pos <= n + 1.2:
        return GHOST_ALPHA
    return GHOST_ALPHA * float(np.clip((n + 2.0 - pos) / 0.8, 0, 1))


def hex255(h):
    return np.array([int(round(x * 255)) for x in hex_rgb(h)], np.float32)


def make_background(th):
    rng = np.random.default_rng(7)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    top, bot = hex255(th["bg_top"]), hex255(th["bg_bot"])
    t = (yy / H)[..., None]
    img = top * (1 - t) + bot * t
    n = rng.random((H // 24 + 2, W // 24 + 2)).astype(np.float32)
    im = Image.fromarray((n * 255).astype("uint8")).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(10))
    img += ((np.asarray(im, np.float32) / 255 - 0.5) * 16)[..., None]
    hx = (xx / W)[..., None]
    band = hex255(th["hdr_l"]) * (1 - hx) + hex255(th["hdr_r"]) * hx
    img = np.where((yy < HEADER_H)[..., None], band, img)
    return np.clip(img, 0, 255).astype(np.uint8)


def bottom_slab(bg):
    crop = bg[SAFE_BOTTOM:H]
    ramp = np.linspace(0, 1, crop.shape[0], dtype=np.float32)
    alpha = (ramp * ramp * (3 - 2 * ramp) * 255).astype(np.uint8)
    return np.dstack([crop, np.repeat(alpha[:, None], W, axis=1)])


def draw_icon(ax, kind, cx, cy, r):
    navy = "#10153a"
    ball = Circle((cx, cy), r, fc="white", ec=navy, lw=3, zorder=5)
    ax.add_patch(ball)
    ax.add_patch(RegularPolygon((cx, cy), 5, radius=r * 0.36, orientation=np.pi, fc=navy, ec="none", zorder=6))


# Club kit colours by logo slug: "#hex", or ("stripes"|"hoops", colour1, colour2)
CLUB_COLORS = {
    "chelsea": "#0315E8", "arsenal": "#FB1116", "liverpool": "#DF1500", "manchester-united": "#EF3000",
    "manchester-city": "#6CABDD", "tottenham-hotspur": "#F4F4F4", "everton": "#003399", "leicester-city": "#003090",
    "real-madrid": "#FFFFFF", "barcelona": ("stripes", "#A50044", "#004D98"), "bayern-munich": "#DC052D",
    "juventus": ("stripes", "#111111", "#FFFFFF"), "ac-milan": ("stripes", "#FB090B", "#111111"), "inter-milan": ("stripes", "#0068A8", "#111111"),
    "atletico-madrid": ("stripes", "#CB3524", "#FFFFFF"), "paris-saint-germain": "#004170", "borussia-dortmund": "#FDE100",
    "benfica": "#E83030", "porto": ("stripes", "#00428C", "#FFFFFF"), "roma": "#8E1F2F",
    "celtic": ("hoops", "#018749", "#FFFFFF"),
    # Scottish clubs (home kit colours)
    "rangers": "#1B458F", "aberdeen": "#C8102E", "heart-of-midlothian": "#7A1F35", "hibernian": "#00703C",
    "queens-park": ("hoops", "#111111", "#FFFFFF"), "dundee": "#1C2D5A", "dundee-united": "#F47920",
    "kilmarnock": ("stripes", "#1D4C9E", "#FFFFFF"), "st-mirren": ("stripes", "#111111", "#FFFFFF"), "motherwell": "#F5A800",
    "falkirk": "#002F6C", "clyde": "#FFFFFF", "stirling-albion": "#D50032", "ayr-united": "#F2F2F2",
    "partick-thistle": ("stripes", "#C8102E", "#FFD200"), "raith-rovers": "#1F2F6B", "morton": ("hoops", "#0C3C8C", "#FFFFFF"),
    "st-johnstone": "#0055A5",
}


LOGO_ALIASES = {"man utd": "manchester-united", "man united": "manchester-united", "man city": "manchester-city",
                "spurs": "tottenham-hotspur", "tottenham": "tottenham-hotspur", "inter": "inter-milan", "psg": "paris-saint-germain",
                "milan": "ac-milan", "atletico": "atletico-madrid", "hearts": "heart-of-midlothian"}


def logo_slug(name):
    import re
    n = name.lower().strip()
    if n in LOGO_ALIASES:
        return LOGO_ALIASES[n]
    n = n.replace("&", "and").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", n).strip("-")


def load_logo(logo_dir, name):
    if not logo_dir:
        return None, False
    fp = os.path.join(logo_dir, logo_slug(name) + ".png")
    if not os.path.exists(fp):
        return None, False
    im = Image.open(fp).convert("RGBA")
    a = np.asarray(im, np.float32) / 255
    op = a[..., 3] > 0.5
    lum = (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2])[op].mean() if op.any() else 0
    w, h = im.size
    side = max(w, h)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(im, ((side - w) // 2, (side - h) // 2))
    return np.asarray(sq), lum > 0.82


LOGO_BOX_W, LOGO_BOX_H = 140, 60


def load_logo_bare(logo_dir, name):
    if not logo_dir:
        return None
    import re as _re
    plain = _re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", "and").replace("'", "")).strip("-")
    fp = os.path.join(logo_dir, plain + ".png")
    if not os.path.exists(fp):
        fp = os.path.join(logo_dir, logo_slug(name) + ".png")
    words = plain.split("-")
    for k in range(1, len(words)):
        if os.path.exists(fp):
            break
        fp = os.path.join(logo_dir, "-".join(words[k:]) + ".png")
    if not os.path.exists(fp):
        return None
    im = Image.open(fp).convert("RGBA")
    bb = im.getchannel("A").getbbox()
    if bb:
        im = im.crop(bb)
    a = np.asarray(im, np.float32) / 255
    op = a[..., 3] > 0.5
    rgb = a[..., :3][op]
    white = a.copy(); white[..., :3] = 1.0
    dark = a.copy(); dark[..., :3] = 0.07
    med = np.median(rgb, axis=0) if len(rgb) else np.zeros(3)
    mono = float((np.abs(rgb - med).max(axis=1) < 0.22).mean()) if len(rgb) else 1.0
    if len(rgb) and float((rgb.max(axis=1) - rgb.min(axis=1)).mean()) < 0.08:
        mono = 1.0
    return dict(orig=a, white=white, dark=dark, aspect=im.size[0] / im.size[1], px=rgb, fill=float(op.mean()), mono=mono)


def logo_variant(lg, face):
    if lg.get("mono", 0) >= 0.6 and len(lg["px"]):
        med = np.median(lg["px"], axis=0)
        l_med = 0.2126 * med[0] ** 2.2 + 0.7152 * med[1] ** 2.2 + 0.0722 * med[2] ** 2.2
        l_bar = rel_lum(tuple(np.array(face[:3])))
        lp_ = 0.2126 * lg["px"][:, 0] ** 2.2 + 0.7152 * lg["px"][:, 1] ** 2.2 + 0.0722 * lg["px"][:, 2] ** 2.2
        two_tone = (lp_ > 0.6).mean() > 0.33 and (lp_ < 0.1).mean() > 0.33
        if not two_tone and (max(l_med, l_bar) + 0.05) / (min(l_med, l_bar) + 0.05) < 1.25:
            return "white" if l_bar < 0.35 else "dark"
    if lg.get("fill", 0) > 0.6 or lg.get("mono", 1) < 0.75:
        return "orig"
    lp = 0.2126 * lg["px"][:, 0] ** 2.2 + 0.7152 * lg["px"][:, 1] ** 2.2 + 0.0722 * lg["px"][:, 2] ** 2.2
    if len(lp) and (lp > 0.6).mean() > 0.12 and (lp < 0.1).mean() > 0.12:
        return "orig"
    face = np.array(face[:3])
    lum_bar = rel_lum(tuple(face))
    lum_px = 0.2126 * lg["px"][:, 0] ** 2.2 + 0.7152 * lg["px"][:, 1] ** 2.2 + 0.0722 * lg["px"][:, 2] ** 2.2
    hi, lo = np.maximum(lum_px, lum_bar), np.minimum(lum_px, lum_bar)
    good = (((hi + 0.05) / (lo + 0.05)) >= 3.0).mean() if len(lum_px) else 1
    if good >= 0.45:
        return "orig"
    return "white" if lum_bar < 0.35 else "dark"


def frame_flag(im, frac=0.06):
    im = np.asarray(im, dtype=float)
    if im.max() > 1.0:
        im = im / 255.0
    if im.shape[2] == 4:
        im = im[..., :3] * im[..., 3:4] + (1 - im[..., 3:4])
    h, w = im.shape[:2]
    b = max(2, int(round(h * frac)))
    out = np.ones((h + 2 * b, w + 2 * b, 3))
    out[b:b + h, b:b + w] = im[..., :3]
    return out


def assign_palette(names, codes, key_vals, n_colors, same_nation):
    need = [k for k, c in enumerate(codes) if same_nation or c not in COUNTRY_COLORS]
    out = {}
    if key_vals is None or not need:
        for j, k in enumerate(need):
            out[k] = j % n_colors
        return out
    ranks = np.array([ranks_of(v) for v in key_vals])
    vis = (ranks < TOP_N + 1).sum(axis=0)
    order = sorted(need, key=lambda k: -vis[k])
    for k in order:
        cost = np.zeros(n_colors)
        for j, c in out.items():
            close = ((np.abs(ranks[:, k] - ranks[:, j]) <= 4) & (ranks[:, k] < TOP_N + 1) & (ranks[:, j] < TOP_N + 1))
            w = (np.abs(ranks[:, k] - ranks[:, j]) <= 1).astype(float) * 3 + close
            cost[c] += float((w * ((ranks[:, k] < TOP_N + 1) | (ranks[:, j] < TOP_N + 1))).sum())
        out[k] = int(np.argmin(cost + 1e-3 * np.arange(n_colors)))
    return out


def make_scene(names, codes, font, flag_dir, th, title_lines, icon_path=None, max_value=0, key_vals=None, logo_dir=None):
    global BAR_MAX_W, LEAD_W0, YEAR_X
    F = fm.FontProperties(fname=font)
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    bg = make_background(th)
    fig.figimage(bg, 0, 0, origin="upper", zorder=0)
    fig.figimage(bottom_slab(bg), 0, 0, origin="upper", zorder=2)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_zorder(1)
    ax.patch.set_alpha(0)
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    canvas = FigureCanvasAgg(fig)
    renderer = canvas.get_renderer()
    shadow = soft_shadow(th["shadow"], th["shadow_a"])
    hdr_shadow = soft_shadow("#000000", 1.4)

    n_digits = len(str(int(round(max_value))))
    val_w = 0
    for dgt in "0123456789":
        ptxt = dgt * n_digits
        probe = ax.text(0, 0, ptxt, fontproperties=F, fontsize=px(VALUE_PX))
        val_w = max(val_w, probe.get_window_extent(renderer).width)
        probe.remove()
    mvp_w = 0
    if TROPHY and TROPHY_ICONS:
        n_max = max((len(cs) for t_ in TROPHY.values() for cs in t_.values()), default=1) if TROPHY_MODE["group"] else 1
        mvp_w = max(mvp_w, TROPHY_GAP + TROPHY_H * (1.25 if n_max == 1 else 0.9 * 0.85 * n_max + 0.2))
    GROW["renderer"] = renderer
    BAR_MAX_W = int(min(480, RIGHT_LIMIT - 8 - VALUE_GAP - val_w - mvp_w - BAR_X0))
    LEAD_W0 = min(400, BAR_MAX_W - 60)
    YEAR_X = BAR_X0 + BAR_MAX_W // 2

    ts = []
    for txt, y in zip(title_lines, (220, 306)):
        t = ax.text(0, y, txt, color=th["title"], fontproperties=F, fontsize=px(TITLE_PX), ha="left", va="center")
        t.set_path_effects(hdr_shadow)
        ts.append(t)
    title_w = max(t.get_window_extent(renderer).width for t in ts)
    icon_im = plt.imread(icon_path) if icon_path else None
    group_w = 2 * ICON_R + ICON_GAP + title_w
    x_start = (W - group_w) / 2
    if x_start < SAFE_X:
        sys.exit(f"header group too wide ({group_w:.0f}px): shorten the title")
    icx, icy = x_start + ICON_R, 262
    if icon_path:
        im = icon_im
        ih, iw = im.shape[:2]
        s = 2 * ICON_R / max(ih, iw)
        hw, hh = iw * s / 2, ih * s / 2
        ax.imshow(im, extent=(icx - hw, icx + hw, icy + hh, icy - hh), interpolation="antialiased", zorder=6)
    else:
        draw_icon(ax, th["icon"], icx, icy, ICON_R)
    for t in ts:
        t.set_x(x_start + 2 * ICON_R + ICON_GAP)

    bg_mid = tuple(((np.array(hex_rgb(th["bg_top"])) + np.array(hex_rgb(th["bg_bot"]))) / 2).tolist())
    chart_bottom = LAST_YC + BAR_H / 2 + 10
    ax.plot([BAR_X0, BAR_X0], [Y0 - 8, chart_bottom], color=th["text"], alpha=0.25, lw=2, zorder=1)
    leader = ax.plot([0, 0], [Y0 - 8, chart_bottom], color=th["accent"], lw=2.6, alpha=0.32, zorder=1,
                     ls=(0, (1.0, 2.2)), dash_capstyle="round")[0]
    year_txt = ax.text(YEAR_X, YEAR_Y, "", color=th["text"], fontproperties=F, fontsize=px(YEAR_PX),
                       ha="center", va="center", zorder=1000)
    year_txt.set_path_effects(shadow)

    timelines = [parse_codes(c) for c in codes]
    codes = [t[-1][1] if t else "" for t in timelines]
    nonblank = [c for c in codes if c]
    same_nation = bool(nonblank) and max(nonblank.count(c) for c in set(nonblank)) > 0.5 * len(codes)
    use_palette = same_nation or "--palette" in sys.argv
    palette_idx = assign_palette(names, codes, key_vals, len(th["palette"]), use_palette)
    art = []
    for k, (name, cc, tl) in enumerate(zip(names, codes, timelines)):
        club = CLUB_COLORS.get(logo_slug(name)) if not cc else None
        pattern = None
        if club is not None:
            if isinstance(club, tuple):
                pattern, c1, c2 = club
                col, col2 = hex_rgb(c1), hex_rgb(c2)
            else:
                col = hex_rgb(club)
        elif cc in COUNTRY_COLORS and not use_palette:
            col = ensure_contrast(hex_rgb(COUNTRY_COLORS[cc]), bg_mid)
        else:
            col = ensure_contrast(hex_rgb(th["palette"][palette_idx[k]]), bg_mid)
        ctl = None
        if name in COLOR_TL:
            ctl = [(y_, hex_rgb(f_), hex_rgb(e_) if e_ else None) for y_, f_, e_ in COLOR_TL[name]]
            col = ctl[0][1]
        bar = FancyBboxPatch((BAR_X0, 0), 10, BAR_H, boxstyle="round,pad=0,rounding_size=14", fc=col, ec="none")
        seg = None
        stripe = None
        if pattern:
            n = 900 if pattern == "stripes" else BAR_H
            idx_ = np.arange(n)
            band = ((idx_ // 26) % 2 == 0) if pattern == "stripes" else ((idx_ // 16) % 2 == 0)
            c_a, c_b = np.array(col), np.array(col2)
            if pattern == "stripes":
                img_ = np.where(band[None, :, None], c_a, c_b) * np.ones((BAR_H, 1, 1))
            else:
                img_ = np.where(band[:, None, None], c_a, c_b) * np.ones((1, 900, 1))
            stripe = ax.imshow(img_, extent=(0, 1, 1, 0), interpolation="nearest")
        glow = [FancyBboxPatch((0, 0), 10, 10, boxstyle=f"round,pad=0,rounding_size={14 + e}", fc=col, ec="none") for e in (6, 13, 22)]
        chip = FancyBboxPatch((0, 0), CHIP_W, CHIP_H, boxstyle="round,pad=0,rounding_size=10", fc=th["chip"], ec="none")
        chip_t = ax.text(0, 0, cc, color="white", fontproperties=F, fontsize=px(CHIP_PX), ha="center", va="center")
        pill = FancyBboxPatch((0, 0), 10, PILL_H, boxstyle="round,pad=0,rounding_size=16", fc=th["pill_bg"], ec="none")
        variants = []
        for y_from, label in NAME_TL.get(name, [(None, name)]):
            pill_t = ax.text(0, 0, label, color=th["pill_fg"], fontproperties=F, fontsize=px(NAME_PX), ha="right", va="center")
            pw = pill_t.get_window_extent(renderer).width + 2 * PILL_PAD
            max_pw = BAR_X0 - PILL_GAP - SAFE_X
            if pw > max_pw:
                pill_t.set_fontsize(pill_t.get_fontsize() * (max_pw - 2 * PILL_PAD) / (pw - 2 * PILL_PAD))
                pw = pill_t.get_window_extent(renderer).width + 2 * PILL_PAD
            variants.append((y_from, label, pw, pill_t.get_fontsize()))
            pill_t.remove()
        pill_t = ax.text(0, 0, variants[0][1], color=th["pill_fg"], fontproperties=F, fontsize=variants[0][3], ha="right", va="center")
        pw = variants[0][2]
        val = ax.text(0, 0, "", color=th["text"], fontproperties=F, fontsize=px(VALUE_PX), ha="left", va="center")
        val.set_path_effects(shadow)
        rec = None
        for p in glow + [bar, chip, pill]:
            ax.add_patch(p)
        if stripe is not None:
            stripe.set_clip_path(bar)
        flags = {}
        for _, code in tl:
            fp = os.path.join(flag_dir, f"{code.lower()}.png") if (flag_dir and code) else None
            if code not in flags:
                flags[code] = None
                if fp and os.path.exists(fp):
                    fim = plt.imread(fp)
                    if use_palette or name in COLOR_TL:
                        fim = frame_flag(fim)
                    flags[code] = ax.imshow(fim, extent=(0, 1, 1, 0), aspect="auto", interpolation="antialiased")
                    flags[code].set_visible(False)
        bare = None
        bare_tl = None
        logo_tl = None
        if "--logo-bare" in sys.argv and name in LOGO_TL:
            logo_tl = [(y_, load_logo_bare(logo_dir, sl_)) for y_, sl_ in LOGO_TL[name]]
            miss_ = [sl_ for (y_, sl_), (_, b_) in zip(LOGO_TL[name], logo_tl) if b_ is None]
            if miss_:
                print("MISSING LOGO", name, miss_)
            bare = next((b_ for _, b_ in logo_tl if b_ is not None), None)
            logo_img, dark_disc = None, False
        elif "--logo-bare" in sys.argv and not cc:
            bare_tl = [(y_, load_logo_bare(logo_dir, lab_)) for y_, lab_ in NAME_TL.get(name, [(None, name)])]
            bare = bare_tl[0][1]
            logo_img, dark_disc = None, False
        else:
            logo_img, dark_disc = (load_logo(logo_dir, name) if not cc else (None, False))
        logo = disc = None
        if bare is not None:
            logo = ax.imshow(bare["orig"], extent=(0, 1, 1, 0), interpolation="antialiased")
        if logo_img is not None:
            disc = Circle((0, 0), LOGO_R, fc=th["chip"] if dark_disc else "#ffffff", ec="none")
            ax.add_patch(disc)
            logo = ax.imshow(logo_img, extent=(0, 1, 1, 0), interpolation="antialiased")
        tro_im = None
        tro_more = []
        if name in TROPHY and TROPHY_ICONS:
            tro_im = ax.imshow(next(iter(TROPHY_ICONS.values())), extent=(0, 1, 1, 0), interpolation="antialiased")
            tro_im.set_visible(False)
            for _ in range(5):
                q_ = ax.imshow(next(iter(TROPHY_ICONS.values())), extent=(0, 1, 1, 0), interpolation="antialiased")
                q_.set_visible(False); tro_more.append(q_)
        a = dict(tro_im=tro_im, tro_more=tro_more, tro_seq=None, tro_last=None, tro_age=0, stars=[], star_n=0, star_pop=0,
                 mvp_im=None, mvp_t=None, mvp_n=0, mvp_pop=0, final_name=name, bar=bar, glow=glow, chip=chip, chip_t=chip_t,
                 pill=pill, pill_t=pill_t, val=val, rec=rec, logo=logo, disc=disc, stripe=stripe,
                 flags=flags, seg=seg, ctl=ctl, bare=bare, bare_tl=bare_tl, logo_tl=logo_tl, cur_col=None, cur_var="orig",
                 timeline=tl, cur=None, flag=None, pw=pw, variants=variants,
                 chips_on=bool(cc) and not (same_nation and len(tl) == 1), has_cc=False)
        set_period(a, None)
        art.append(a)
    if TROPHY and TROPHY_ICONS:
        items, seen_ = [], []
        used_ = {c_ for t_ in TROPHY.values() for cs in t_.values() for c_ in cs}
        for c, lab in TROPHY_LEGEND:
            if c not in used_:
                continue
            im_ = TROPHY_ICONS.get(c)
            if im_ is not None and not any(im_ is q for q in seen_):
                items.append((im_, lab)); seen_.append(im_)
        lh, lpx, lgap, igap = 40, 23, 30, 8
        texts = [ax.text(0, 0, lab, color=th["text"], fontproperties=F, fontsize=px(lpx), ha="left", va="center", alpha=0.9)
                 for _, lab in items]
        tw = [t.get_window_extent(renderer).width for t in texts]
        iws = [lh * im.shape[1] / im.shape[0] for im, _ in items]
        total = sum(iws) + sum(tw) + igap * len(items) + lgap * (len(items) - 1)
        if total > W - 2 * SAFE_X:
            k_ = (W - 2 * SAFE_X) / total
            lh *= k_; iws = [q * k_ for q in iws]; tw = [q * k_ for q in tw]; lgap *= k_; igap *= k_
            for t in texts: t.set_fontsize(t.get_fontsize() * k_)
            total = W - 2 * SAFE_X
        x = (W - total) / 2
        ly = LEGEND_Y
        for (im, _), t, w_, iw_ in zip(items, texts, tw, iws):
            ax.imshow(im, extent=(x, x + iw_, ly + lh / 2, ly - lh / 2), interpolation="antialiased", zorder=7)
            t.set_position((x + iw_ + igap, ly + 1)); t.set_zorder(7)
            x += iw_ + igap + w_ + lgap
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    return fig, ax, year_txt, leader, art


def set_period(a, year):
    code = a["timeline"][0][1] if year is None and a["timeline"] else code_at(a["timeline"], year if year is not None else 0)
    if code == a["cur"]:
        return
    if a["flag"] is not None:
        a["flag"].set_visible(False)
    a["cur"] = code
    a["flag"] = a["flags"].get(code)
    a["chip_t"].set_text(code)
    a["has_cc"] = a["chips_on"] and bool(code)


def row_parts(a):
    parts = [a["bar"], a["pill"], a["pill_t"], a["val"]]
    if a.get("logo") is not None:
        parts += [q for q in (a["disc"], a["logo"]) if q is not None]
    if a["flag"] is not None:
        parts.append(a["flag"])
    elif a["has_cc"]:
        parts += [a["chip"], a["chip_t"]]
    return parts


GROW = {"lo": 1.0, "hi": 2.0}


def draw_frame(year_txt, leader, art, frame):
    label, v, r = frame[:3]
    txt_ = YEAR_LABELS.get(label, str(label))
    year_txt.set_text(txt_)
    year_txt.set_fontsize(px(YEAR_PX * min(1.0, max(0.42, 4.6 / max(len(txt_), 1)))))
    vmax = max(v.max(), 1)
    p = float(np.clip((vmax - GROW["lo"]) / max(GROW["hi"] - GROW["lo"], 1e-6), 0, 1))
    lead_w = LEAD_W0 + p * (BAR_MAX_W - LEAD_W0)
    scale = lead_w / vmax
    GROW["scale"] = scale
    leader.set_xdata([BAR_X0 + lead_w + 7] * 2)
    z_base = np.empty(len(v))
    z_base[np.argsort(v, kind="stable")] = np.arange(len(v)) * 10 + 4
    for i, a in enumerate(art):
        pos = r[i]
        alpha = row_alpha(pos)
        if "--hide-zero" in sys.argv:
            alpha *= float(np.clip(v[i] / 0.35, 0, 1))
        visible = alpha > 0.003
        set_period(a, label)
        if a.get("logo_tl"):
            nb = None
            for y_, b_ in a["logo_tl"]:
                if label >= y_ and b_ is not None:
                    nb = b_
            if nb is not None and nb is not a["bare"] and a["logo"] is not None:
                a["bare"] = nb; a["cur_col"] = None; a["cur_var"] = "orig"
                a["logo"].set_data(nb["orig"])
        for f_ in a["flags"].values():
            if f_ is not None:
                f_.set_visible(False)
        parts = row_parts(a)
        for k, q in enumerate(a["glow"]):
            q.set_zorder(z_base[i] - 2 + k * 0.1)
        if a.get("stripe") is not None:
            a["stripe"].set_zorder(z_base[i] + 0.5)
        for k, q in enumerate((a["bar"], a["chip"], a["chip_t"], a["flag"], a["pill"], a["pill_t"], a["val"], a.get("disc"), a.get("logo"))):
            if q is not None:
                q.set_zorder(z_base[i] + k)
        for q in parts + a["glow"] + [a["chip"], a["chip_t"]]:
            q.set_visible(False)
        if a.get("stripe") is not None:
            a["stripe"].set_visible(False)
        if a.get("tro_im") is not None:
            a["tro_im"].set_visible(False)        # hidden unless the pop code below shows it (no frozen icons)
        if not visible:
            continue
        for q in parts:
            q.set_visible(True)
        yc = ypos(pos)
        w = max(v[i] * scale, (LOGO_BOX_W + 28) if a.get("bare") is not None else 90)
        a["bar"].set_bounds(BAR_X0, yc - BAR_H / 2, w, BAR_H)
        if a.get("stripe") is not None:
            a["stripe"].set_extent((BAR_X0, BAR_X0 + 900, yc + BAR_H / 2, yc - BAR_H / 2))
        if a.get("ctl"):
            cur = a["ctl"][0]
            for c_ in a["ctl"]:
                if label >= c_[0]:
                    cur = c_
            face = (0.30, 0.30, 0.33) if v[i] <= 0.02 and "--stub-grey" in sys.argv else cur[1]
            edge = cur[2]
            if a["cur_col"] != (face, edge):
                a["cur_col"] = (face, edge)
                a["bar"].set_facecolor(face)
                a["bar"].set_edgecolor(edge if edge else "none")
                a["bar"].set_linewidth(4 if edge else 0)
                for q in a["glow"]:
                    q.set_facecolor(face)
                if a.get("bare") is not None:
                    var = logo_variant(a["bare"], face)
                    if var != a["cur_var"]:
                        a["cur_var"] = var
                        a["logo"].set_data(a["bare"][var])
        lead_f = float(np.clip(1 - pos, 0, 1))
        for q, e, base_a in zip(a["glow"], (6, 13, 22), (0.16, 0.10, 0.06)):
            if lead_f > 0.01:
                q.set_visible(True)
                q.set_bounds(BAR_X0 - e, yc - BAR_H / 2 - e, w + 2 * e, BAR_H + 2 * e)
                q.set_alpha(base_a * lead_f * alpha)
        cx0 = BAR_X0 + w - CHIP_INSET - CHIP_W
        if a.get("bare") is not None:
            asp = a["bare"]["aspect"]
            lw_ = min(LOGO_BOX_W, LOGO_BOX_H * asp)
            lh_ = lw_ / asp
            x1_ = BAR_X0 + w - 14
            if a["flag"] is not None:
                x1_ = cx0 - 12
                lw_ = min(96, LOGO_BOX_H * 0.85 * asp); lh_ = lw_ / asp
            a["logo_short"] = x1_ - lw_ < BAR_X0 + 10
            a["logo"].set_extent((x1_ - lw_, x1_, yc + lh_ / 2, yc - lh_ / 2))
        elif a.get("logo") is not None:
            lx = BAR_X0 + w - 10 - LOGO_R
            a["disc"].set_center((lx, yc))
            s_ = LOGO_R * 0.78
            a["logo"].set_extent((lx - s_, lx + s_, yc + s_, yc - s_))
        if a["flag"] is not None:
            if a.get("cur") in SQUARE_FLAGS:
                a["flag"].set_extent((cx0 + CHIP_W - CHIP_H, cx0 + CHIP_W, yc + CHIP_H / 2, yc - CHIP_H / 2))
            else:
                a["flag"].set_extent((cx0, cx0 + CHIP_W, yc + CHIP_H / 2, yc - CHIP_H / 2))
        elif a["has_cc"]:
            a["chip"].set_bounds(cx0, yc - CHIP_H / 2, CHIP_W, CHIP_H)
            a["chip_t"].set_position((cx0 + CHIP_W / 2, yc + 2))
        a["pill"].set_bounds(BAR_X0 - PILL_GAP - a["pw"], yc - PILL_H / 2, a["pw"], PILL_H)
        a["pill_t"].set_position((BAR_X0 - PILL_GAP - PILL_PAD, yc + 2))
        a["val"].set_position((BAR_X0 + w + VALUE_GAP, yc + 2))
        a["val"].set_text(f"{max(int(round(v[i])), 0)}")
        for q in parts:
            q.set_alpha(alpha)
        if a.get("logo_short") and a.get("logo") is not None:
            a["logo"].set_alpha(0)
        if a.get("tro_im") is not None:
            tr = TROPHY.get(a["final_name"], {})
            seq = a["tro_seq"]
            if seq is None:
                seq = []
                a["tro_seq"] = seq
            yrs = sorted(tr)
            if not seq and VALS_AT:
                y_first = min(y_ for (n_, y_) in VALS_AT if n_ == a["final_name"])
                run_ = VALS_AT[(a["final_name"], y_first)]       # count at the first data point, then add trophies in order
                for y_ in yrs:
                    if y_ <= y_first:
                        continue
                    for j, c_ in enumerate(tr[y_]):
                        seq.append((run_ + j + 0.5, c_))
                    run_ += len(tr[y_])
            cur = None
            for th_, c_ in seq:
                if v[i] >= th_ - 1e-6:
                    cur = (th_, c_)
            if cur != a["tro_last"]:
                a["tro_last"] = cur; a["tro_age"] = 0
            else:
                a["tro_age"] += 1
            age = a["tro_age"]
            show = cur is not None and age < TROPHY_SHOW and alpha > 0.3
            a["tro_im"].set_visible(show)
            if show:
                img = TROPHY_ICONS.get(cur[1])
                if img is not None and a["tro_im"].get_array() is not img:
                    a["tro_im"].set_data(img)
                pop = 0.35 + 0.95 * min(1, age / 4) if age < 4 else (1.25 - 0.25 * min(1, (age - 4) / 6))
                fade = 1.0 if age < TROPHY_SHOW - 10 else max(0.0, (TROPHY_SHOW - age) / 10)
                txt = a["val"].get_text()
                if txt not in TXT_W:
                    TXT_W[txt] = a["val"].get_window_extent(GROW["renderer"]).width
                ih = TROPHY_H * pop
                iw = ih * img.shape[1] / img.shape[0]
                x0 = BAR_X0 + w + VALUE_GAP + TXT_W[txt] + TROPHY_GAP
                a["tro_im"].set_extent((x0, x0 + iw, yc + ih / 2, yc - ih / 2))
                a["tro_im"].set_zorder(a["val"].get_zorder() + 1)
                a["tro_im"].set_alpha(alpha * fade)
        if a.get("stripe") is not None:
            a["stripe"].set_visible(True)
            a["stripe"].set_alpha(alpha)


class EventLayer:
    W_, H_ = 520, 136
    X0, Y0 = (1080 - 520) // 2, 1330

    def __init__(self, ax, F, th, events, frames, names, art):
        self.items = []
        for ev in events:
            start = next((k for k, fr in enumerate(frames) if fr[0] >= ev["year"]), None)
            if start is None:
                sys.exit(f"event year {ev['year']} is outside the data")
            card = FancyBboxPatch((self.X0, self.Y0), self.W_, self.H_, boxstyle="round,pad=0,rounding_size=22",
                                  fc=th["accent"], ec="none", zorder=1100)
            card.set_path_effects([patheffects.SimplePatchShadow(offset=(0, -4), shadow_rgbFace="#000000", alpha=0.25),
                                   patheffects.Normal()])
            ax.add_patch(card)
            ink = th["pill_fg"] if rel_lum(hex_rgb(th["accent"])) > 0.5 else "#ffffff"
            tag = ax.text(self.X0 + 26, self.Y0 + 34, YEAR_LABELS.get(ev["year"], str(ev["year"])), color=ink, alpha=0.8,
                          fontproperties=F, fontsize=px(26), ha="left", va="center", zorder=1101)
            body = ax.text(self.X0 + 26, self.Y0 + 88, self._wrap(ax, F, ev["text"]), color=ink,
                           fontproperties=F, fontsize=px(31), ha="left", va="center", linespacing=1.15, zorder=1101)
            ring = None
            if ev["who"]:
                if ev["who"] not in names:
                    sys.exit(f"event highlight '{ev['who']}' is not a column name")
                ring = FancyBboxPatch((0, 0), 10, 10, boxstyle="round,pad=0,rounding_size=18", fc="none",
                                      ec=th["accent"], lw=5, zorder=1050)
                ax.add_patch(ring)
            self.items.append(dict(start=start, end=start + int(EVENT_SECONDS * FPS), card=card, tag=tag,
                                   body=body, ring=ring, row=names.index(ev["who"]) if ev["who"] else None, art=art))
        self.update(0)

    def _wrap(self, ax, F, text):
        r = ax.figure.canvas.get_renderer()
        words, lines, cur = text.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            probe = ax.text(0, 0, t, fontproperties=F, fontsize=px(31))
            wide = probe.get_window_extent(r).width > self.W_ - 52
            probe.remove()
            if wide and cur:
                lines.append(cur)
                cur = w
            else:
                cur = t
        lines.append(cur)
        if len(lines) > 2:
            sys.exit(f"event text too long for two lines: {text!r}")
        return "\n".join(lines)

    def parts(self):
        out = []
        for it in self.items:
            out += [q for q in (it["card"], it["tag"], it["body"]) if q.get_visible()]
        return out

    def update(self, i):
        for it in self.items:
            if it["start"] <= i < it["end"]:
                a = min(1.0, (i - it["start"] + 1) / EVENT_FADE, (it["end"] - i) / EVENT_FADE)
                rise = (1 - min(1.0, (i - it["start"] + 1) / EVENT_FADE)) * 14
            else:
                a, rise = 0.0, 0
            vis = a > 0.01
            it["card"].set_visible(vis)
            it["card"].set_y(self.Y0 + rise)
            it["card"].set_alpha(0.96 * a)
            it["tag"].set_visible(vis)
            it["tag"].set_alpha(0.8 * a)
            it["tag"].set_y(self.Y0 + 34 + rise)
            it["body"].set_visible(vis)
            it["body"].set_alpha(a)
            it["body"].set_y(self.Y0 + 88 + rise)
            if it["ring"] is not None:
                bar = it["art"][it["row"]]["bar"]
                on = vis and bar.get_visible() and (bar.get_alpha() or 1) > 0.5
                it["ring"].set_visible(on)
                if on:
                    e = 7
                    it["ring"].set_bounds(bar.get_x() - e, bar.get_y() - e, bar.get_width() + 2 * e, bar.get_height() + 2 * e)
                    pulse = 0.55 + 0.45 * np.sin((i - it["start"]) / FPS * 2 * np.pi * 1.2) ** 2
                    it["ring"].set_alpha(a * pulse)


class EngageLayer:
    SPLASH_FULL, SPLASH_OUT = int(os.environ.get("SPLASH_FULL", 34)), 14
    LOOP_IN = 14

    def __init__(self, ax, F, th, frames, art, question, n_hold_end):
        self.ax, self.th, self.frames, self.art = ax, th, frames, art
        self.n = len(frames)
        self.end_start = self.n - self.LOOP_IN
        lines = [x.strip() for x in question.split("|")][:2]
        self.panel = FancyBboxPatch((SAFE_X + 10, 0), W - 2 * SAFE_X - 20, 330, boxstyle="round,pad=0,rounding_size=34",
                                    fc=th["hdr_l"], ec=th["rule"], lw=5, zorder=2000)
        self.panel.set_path_effects([patheffects.SimplePatchShadow(offset=(0, -8), shadow_rgbFace="#000000", alpha=0.35),
                                     patheffects.Normal()])
        ax.add_patch(self.panel)
        r = ax.figure.canvas.get_renderer()
        size = 80
        while True:
            probe = [ax.text(0, 0, t, fontproperties=F, fontsize=px(size)) for t in lines]
            wmax = max(pr.get_window_extent(r).width for pr in probe)
            for pr in probe:
                pr.remove()
            if wmax <= W - 2 * SAFE_X - 110 or size <= 50:
                break
            size -= 2
        self.q = [ax.text(W / 2, 0, t, color="#ffffff", fontproperties=F, fontsize=px(size), ha="center", va="center",
                          zorder=2001) for t in lines]
        for t in self.q:
            t.set_path_effects(soft_shadow(strength=1.4))
        self.qsize = size
        self.arrows, self.flashes = [], []
        for a in art:
            tri = RegularPolygon((0, 0), 3, radius=17, orientation=np.pi, fc="#ffffff", ec="none", zorder=1150)
            tri.set_visible(False)
            ax.add_patch(tri)
            fl = FancyBboxPatch((0, 0), 10, BAR_H, boxstyle="round,pad=0,rounding_size=14", fc="#ffffff", ec="none",
                                zorder=1140)
            fl.set_visible(False)
            ax.add_patch(fl)
            self.arrows.append(tri)
            self.flashes.append(fl)
        self.badge = FancyBboxPatch((0, 0), 150, 50, boxstyle="round,pad=0,rounding_size=25", fc="#ffffff", ec="none",
                                    zorder=1160)
        self.badge.set_visible(False)
        ax.add_patch(self.badge)
        bcol = th["accent"] if rel_lum(hex_rgb(th["accent"])) < 0.5 else th["pill_fg"]
        self.badge_t = ax.text(0, 0, "NEW #1", color=bcol, fontproperties=F, fontsize=px(30), ha="center",
                               va="center", zorder=1161)
        self.badge_t.set_visible(False)
        self._plan_pops()
        self.broken = []

    def _plan_pops(self):
        rk = np.array([np.floor(fr[2] + 0.5) for fr in self.frames])
        self.pop_start = [[] for _ in self.art]
        self.lead_start = []
        for i in range(1, self.n):
            for j in range(len(self.art)):
                if rk[i, j] < rk[i - 1, j] and rk[i, j] <= TOP_N - 1:
                    self.pop_start[j].append(i)
            if np.argmin(rk[i]) != np.argmin(rk[i - 1]) and i > 2:
                self.lead_start.append((i, int(np.argmin(rk[i]))))
        lead_now = np.argmin(rk, axis=1)
        raw = np.array([fr[2] for fr in self.frames], dtype=float)
        settled = np.all(np.abs(raw - np.round(raw)) < 0.02, axis=1)
        keep = []
        for s0, j in self.lead_start:
            run = 0
            while s0 + run < self.n and lead_now[s0 + run] == j:
                run += 1
            if settled[s0:s0 + run].any() or s0 + run >= self.n:
                keep.append((s0, j))
        self.lead_start = keep

    def parts(self):
        out = [t for t in self.q if t.get_visible()]
        out += [t for t in (self.badge_t,) if t.get_visible()]
        return out

    def _splash_alpha(self, i):
        if i < self.SPLASH_FULL:
            return 1.0, 0.0
        if i < self.SPLASH_FULL + self.SPLASH_OUT:
            t = (i - self.SPLASH_FULL) / self.SPLASH_OUT
            return 1.0 - smooth(t), smooth(t)
        if i >= self.end_start:
            t = (i - self.end_start + 1) / self.LOOP_IN
            return smooth(min(t, 1.0)), 0.0
        return 0.0, 0.0

    def update(self, i):
        a, out = self._splash_alpha(i)
        cy = 1010 - out * 380
        sc = 1.0 - 0.25 * out
        vis = a > 0.01
        ph = 330 * sc
        self.panel.set_visible(vis)
        self.panel.set_bounds(SAFE_X + 10 + (1 - sc) * 480, cy - ph / 2, (W - 2 * SAFE_X - 20) * sc, ph)
        self.panel.set_alpha(0.97 * a)
        dy = 96 * sc if len(self.q) == 2 else 0
        for k, t in enumerate(self.q):
            t.set_visible(vis)
            t.set_alpha(a)
            t.set_fontsize(px(self.qsize * sc))
            t.set_y(cy - dy / 2 + k * dy + 4)
        POP = 20
        for j, a_ in enumerate(self.art):
            starts = [s for s in self.pop_start[j] if 0 <= i - s < POP]
            bar = a_["bar"]
            on = bool(starts) and bar.get_visible() and (bar.get_alpha() or 1) > 0.6
            self.arrows[j].set_visible(on)
            self.flashes[j].set_visible(on)
            if on:
                t = (i - starts[-1]) / POP
                yc = bar.get_y() + bar.get_height() / 2
                self.arrows[j].xy = (BAR_X0 + 30, yc - 6 * (1 - t))
                self.arrows[j].set_alpha(1.0 - t ** 2)
                self.flashes[j].set_bounds(bar.get_x(), bar.get_y(), bar.get_width(), bar.get_height())
                self.flashes[j].set_alpha(0.38 * (1 - t))
                self.flashes[j].set_zorder(bar.get_zorder() + 0.5)
                self.arrows[j].set_zorder(bar.get_zorder() + 0.6)
        BADGE = 45
        lead = [ls for ls in self.lead_start if 0 <= i - ls[0] < BADGE]
        on = bool(lead)
        self.badge.set_visible(on); self.badge_t.set_visible(on)
        if on:
            s0, j = lead[-1]
            t = (i - s0) / BADGE
            bar = self.art[j]["bar"]
            yc = bar.get_y() + bar.get_height() / 2
            pop = 1.0 + 0.25 * max(0.0, 1 - t * 6)
            bw, bh = 150 * pop, 50 * pop
            x0 = BAR_X0 + 58
            self.badge.set_bounds(x0, yc - bh / 2, bw, bh)
            fade = min(1.0, (1 - t) * 4)
            self.badge.set_alpha(fade); self.badge_t.set_alpha(fade)
            self.badge_t.set_position((x0 + bw / 2, yc + 2)); self.badge_t.set_fontsize(px(30 * pop))
            self.badge.set_zorder(bar.get_zorder() + 0.7); self.badge_t.set_zorder(bar.get_zorder() + 0.8)
            self.arrows[j].set_visible(False)


def check_safe_zones(fig, canvas, year_txt, leader, art, frames, step=6, events=None, engage=None):
    bad = 0
    renderer = canvas.get_renderer()
    for idx in range(0, len(frames), step):
        draw_frame(year_txt, leader, art, frames[idx])
        if events:
            events.update(idx)
        if engage:
            engage.update(idx)
        canvas.draw()
        items = [t for t in fig.axes[0].texts if t.get_text() and t.get_visible()]
        items += events.parts() if events else []
        items += [p for a in art for p in row_parts(a) if p.get_visible()]
        for p in items:
            bb = p.get_window_extent(renderer)
            y_top, y_bot = H - bb.y1, H - bb.y0
            al = p.get_alpha()
            al = 1.0 if al is None else al
            bottom_ok = y_bot <= SAFE_BOTTOM or al <= GHOST_ALPHA + 0.01
            if bb.x0 < SAFE_X - 0.5 or bb.x1 > RIGHT_LIMIT + 0.5 or y_top < SAFE_TOP or not bottom_ok:
                bad += 1
                if bad <= 12:
                    print(f"SAFE-ZONE VIOLATION frame {idx}: {getattr(p, 'get_text', lambda: type(p).__name__)()!r} "
                          f"x {bb.x0:.0f}-{bb.x1:.0f}, y {y_top:.0f}-{y_bot:.0f}, alpha {al:.2f}")
    if bad:
        sys.exit(f"{bad} safe-zone violations")
    print("safe-zone check passed")


def opt(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


def main():
    global FRAMES_PER_YEAR, SEASON_LABELS, TOP_N, ROW_H, BAR_H, ROW0_YC, LAST_YC
    SEASON_LABELS = "--season-labels" in sys.argv
    names_ = ("--font", "--flags", "--topic", "--title", "--theme", "--icon", "--icons-dir", "--fpy", "--seconds", "--logos", "--question", "--trophy-icons")
    o = {n: opt(n) for n in names_}
    skip = {v for v in o.values() if v}
    args = [a for a in sys.argv[1:] if not a.startswith("--") and a not in skip]
    src, dst = args[0], args[1]
    preview = "--preview" in sys.argv

    csv_topic, names, codes, years, vals, events_spec = load(src)
    FLAG_DIR["d"] = o["--flags"]
    if "--check-flags" in sys.argv:
        need = sorted({c for raw in codes for _, c in parse_codes(raw) if c})
        missing = [c for c in need if not (o["--flags"] and os.path.exists(os.path.join(o["--flags"], f"{c.lower()}.png")))]
        print("flags needed:", ", ".join(c.lower() for c in need) or "none")
        print("MISSING:", ", ".join(f"{c.lower()}.png" for c in missing) if missing else "none")
        no_logo = []
        if o["--logos"]:
            for n, raw in zip(names, codes):
                slugs = [s for _, s in LOGO_TL.get(n, [])] or ([logo_slug(n)] if not raw else [])
                for s in slugs:
                    if not os.path.exists(os.path.join(o["--logos"], s + ".png")):
                        no_logo.append(f"{s}.png ({n})")
            print("LOGOS MISSING:", ", ".join(sorted(set(no_logo))) if no_logo else "none")
        sys.exit(1 if (missing or no_logo) else 0)
    font = find_font(o["--font"])
    if o["--trophy-icons"] and TROPHY:
        cache_ = {}
        for c_, cands in TROPHY_FILES.items():
            for f_ in cands:
                pth = os.path.join(o["--trophy-icons"], f_ + ".png")
                if os.path.exists(pth):
                    if pth not in cache_:
                        cache_[pth] = plt.imread(pth)
                    TROPHY_ICONS[c_] = cache_[pth]; break
        miss_ = sorted({c_ for t_ in TROPHY.values() for cs in t_.values() for c_ in cs} - set(TROPHY_ICONS))
        print("trophy icons:", sorted(TROPHY_ICONS), "missing:", miss_)
        LAST_YEAR["y"] = years[-1]
        for n_, row_ in zip(names, vals.T):
            for k_, y_ in enumerate(years):
                VALS_AT.setdefault((n_, y_), float(row_[k_]))   # duplicate year labels: keep the first (start) row   # duplicate year labels (zero row): the later row wins
    topic = o["--topic"] or csv_topic or "football"
    theme_name = o["--theme"] or pick_theme(topic)
    th = THEMES[theme_name]
    title_lines = (o["--title"] or "Title|Here").split("|")[:2]
    icon_path = o["--icon"]
    GROW["lo"], GROW["hi"] = float(vals[0].max()), float(vals.max())
    secs = float(o["--seconds"] or 33)
    frames = build_timeline_paced(years, vals, int(secs * FPS), hold_end=int(os.environ.get("HOLD_END", 50)) + EngageLayer.LOOP_IN)
    print(f"engage pacing: {len(frames)} frames ({len(frames) / FPS:.1f} s)")
    fig, ax, year_txt, leader, art = make_scene(names, codes, font, o["--flags"], th, title_lines,
                                                icon_path=icon_path, max_value=float(vals.max()), key_vals=vals,
                                                logo_dir=o["--logos"])
    canvas = FigureCanvasAgg(fig)
    events = EventLayer(ax, fm.FontProperties(fname=font), th, events_spec, frames, names, art) if events_spec else None
    q = o["--question"] or QUESTION["text"]
    engage = EngageLayer(ax, fm.FontProperties(fname=font), th, frames, art, q, 50)
    check_safe_zones(fig, canvas, year_txt, leader, art, frames, events=events, engage=engage)

    if preview:
        os.makedirs(dst, exist_ok=True)
        n = len(frames)
        picks = [0, n // 3, 2 * n // 3, n - 1] + ([it["start"] + 30 for it in events.items] if events else [])
        picks += [40, n - 60] + [ls[0] + 8 for ls in engage.lead_start[:2]]
        for i, idx in enumerate(picks):
            draw_frame(year_txt, leader, art, frames[idx])
            if events:
                events.update(idx)
            engage.update(idx)
            fig.savefig(f"{dst}/frame_{i}.png", dpi=100)
        print("preview frames:", picks, "of", n, f"({n / FPS:.1f} s)")
        return

    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
         "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
         "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", dst],
        stdin=subprocess.PIPE)
    for i, fr in enumerate(frames):
        draw_frame(year_txt, leader, art, fr)
        if events:
            events.update(i)
        engage.update(i)
        canvas.draw()
        ff.stdin.write(canvas.buffer_rgba().tobytes())
        if i % 200 == 0:
            print(f"{i}/{len(frames)}", flush=True)
    ff.stdin.close()
    ff.wait()
    print("done", len(frames) / FPS, "seconds")


if __name__ == "__main__":
    main()
