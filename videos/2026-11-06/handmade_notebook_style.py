"""TrekJon "Hand-made Notebook" - the Notebook skin rebuilt to look less computer-made, with colour presets.
(Working copy of graph-race/handmade_notebook_style.py from the Project, plus the new heather and claret presets.)
Usage: exactly the same arguments as goals_race_vertical.py. Keep this file next to it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from PIL import Image, ImageFilter

import goals_race_vertical as g

PRESETS = {
    "butter": dict(header="#F3D36B", ink="#1D3E8F", accent="#E4572E", paper_top="#F8F3E6", paper_bot="#EEE5D0",
                   rules="#AFC0E3", margin="#E4572E", title="#1D3E8F", tape="#8FA8D8", pill="#FFFDF7",
                   text="#16285e"),
    # Heather & Whisky (Scottish football): heather-purple header, ivory sheet, plum ink, whisky-gold accent
    "heather": dict(icon="#FFFFFF", header="#4B3A6B", ink="#2B2340", accent="#D9A21B", paper_top="#F8F5EE", paper_bot="#EEE8DC",
                    rules="#CBC2DD", margin="#8E6BB3", title="#FFFFFF", tape="#B9A6D6", pill="#FFFDF8",
                    text="#2B2340"),
    # Rink (NHL): navy header, cool ice-white sheet, navy ink, goal-line red accent
    "rink": dict(icon="#FFFFFF", header="#0C2340", ink="#0C2340", accent="#C8102E", paper_top="#F5F8FB", paper_bot="#E6EDF3",
                 rules="#BCD0E3", margin="#C8102E", title="#FFFFFF", tape="#9EBFDE", pill="#FFFFFF", text="#0C2340"),
    # Claret & Gold (managers): claret header, warm ivory sheet, near-black ink, old-gold accent
    "claret": dict(icon="#FFFFFF", header="#5E1A2E", ink="#24161B", accent="#C9A227", paper_top="#FAF6EE", paper_bot="#F0E8DA",
                   rules="#DCCBBE", margin="#C9A227", title="#FFFFFF", tape="#D9B8A4", pill="#FFFDF8",
                   text="#24161B"),
}
P = PRESETS[os.environ.get("NB_PRESET", "butter").lower()]
INK, ACCENT = P["ink"], P["accent"]
SKIN = dict(dark=False, texture="notebook", bg_top=P["paper_top"], bg_bot=P["paper_bot"], glow="#fffdf6",
            hdr_l=P["header"], hdr_r=P["header"], rule=INK, accent=ACCENT, title=P["title"],
            pill_bg=P["pill"], pill_fg=P["text"], chip=P["text"], text=P["text"], shadow="#6b5a2a", shadow_a=0.22)
if P.get("dark"):
    SKIN.update(dark=True, shadow="#000000", shadow_a=0.45, glow=P["paper_top"])

AMP_FILL, AMP_INK, AMP_INK2, AMP_PILL = 1.4, 1.0, 1.3, 0.7
BOIL_EVERY, BOIL_VARIANTS, BOIL_MIX = 8, 3, 0.25
INTRO_DELAY, INTRO_STAGGER, INTRO_LEN = 3, 2, 16
OUTRO_STAGGER, OUTRO_LEN = 1, 12
POP_LEN, POP_HOP = 12, 9
PUSH_IN, NUDGE, NUDGE_W = 0.02, 0.006, 9.0
GRAIN_EVERY = 3
TILT = np.radians(0.35)

STATE = {"rows": [], "underline": None, "year_w": 200, "engage": None, "events": None, "art": None,
         "fig": None, "bg": None, "grain": None, "lead_frames": [], "pops": None, "tex_cache": {}}


def wob(seed):
    rng = np.random.default_rng(seed)
    ph = rng.random(4) * 2 * np.pi
    per = (131.0, 53.0, 23.0, 11.0)
    amp = (1.0, 0.5, 0.25, 0.08)
    return lambda s: sum(a * np.sin(2 * np.pi * s / p + f) for a, p, f in zip(amp, per, ph))


def boiled(seed):
    base = wob(seed)
    var = [wob(seed * 31 + 7 + b) for b in range(BOIL_VARIANTS)]
    return [(lambda s, v=v: base(s) + BOIL_MIX * v(s)) for v in var]


def rrect(x, y, w, h, r, step=7.0):
    r = max(1.0, min(r, w / 2, h / 2))
    pts, nrm = [], []

    def line(a, b, n):
        L = np.hypot(b[0] - a[0], b[1] - a[1])
        k = max(2, int(L / step))
        for i in range(k):
            t = i / k
            pts.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)); nrm.append(n)

    def arc(cx, cy, a0, a1):
        k = max(3, int(r * np.pi / 2 / step))
        for i in range(k):
            a = np.radians(a0 + (a1 - a0) * i / k)
            pts.append((cx + r * np.cos(a), cy + r * np.sin(a))); nrm.append((np.cos(a), np.sin(a)))

    line((x + r, y), (x + w - r, y), (0, -1)); arc(x + w - r, y + r, -90, 0)
    line((x + w, y + r), (x + w, y + h - r), (1, 0)); arc(x + w - r, y + h - r, 0, 90)
    line((x + w - r, y + h), (x + r, y + h), (0, 1)); arc(x + r, y + h - r, 90, 180)
    line((x, y + h - r), (x, y + r), (-1, 0)); arc(x + r, y + r, 180, 270)
    return np.array(pts), np.array(nrm)


def edge_keys(p, n, x, y, w, h, r):
    px_, py_ = p[:, 0], p[:, 1]
    horiz = np.abs(n[:, 1]) >= np.abs(n[:, 0])
    right_end = px_ > x + w - r - 1
    return np.where(horiz, np.where(right_end, (px_ - (x + w)) + 7000, px_ - x) + (n[:, 1] > 0) * 3000,
                    (py_ - y) + (n[:, 0] > 0) * 9000 + 5000)


def sketch(x, y, w, h, r, fn, amp, overshoot=0, ragged=None):
    p, n = rrect(x, y, w, h, r)
    off = fn(edge_keys(p, n, x, y, w, h, r)) * amp
    if ragged is not None:
        right = p[:, 0] > x + w - r - 1
        off = off + right * ragged(p[:, 1] - y) * 3.2
    q = p + n * off[:, None]
    if overshoot:
        q = np.vstack([q, q[:overshoot]])
    return q


def ease(t):
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3 - 2 * t)


def highlighter_texture(col, seed, width=900):
    rng = np.random.default_rng(seed)
    h = g.BAR_H
    c = np.array(g.hex_rgb(col))
    yy, xx = np.mgrid[0:h, 0:width].astype(np.float32)
    a = np.zeros((h, width), np.float32)
    for k in range(3):
        y0 = k * h / 3 - 4 + rng.uniform(-2.5, 2.5) + np.sin(xx / rng.uniform(140, 260) + rng.uniform(0, 6)) * 1.6
        y1 = y0 + h / 3 + 8 + rng.uniform(-2, 2)
        a += 0.5 * np.clip((yy - y0) / 1.8, 0, 1) * np.clip((y1 - yy) / 1.8, 0, 1)
    streak = 0.5 + 0.5 * np.sin(yy / 2.4 + np.sin(xx / 57.0 + seed) * 1.7)
    grain = np.asarray(Image.fromarray((rng.random((h // 2 + 2, width // 5 + 2)) * 255).astype("uint8"))
                       .resize((width, h), Image.BICUBIC), np.float32) / 255
    press = 0.94 + 0.06 * np.sin(xx / 97.0 + seed * 0.7)
    alpha = np.clip(0.60 + a * 0.45, 0, 0.97) * (0.90 + 0.05 * streak + 0.06 * grain) * press
    img = np.zeros((h, width, 4), np.float32)
    shade = (0.90 + 0.10 * (1 - np.clip(a - 0.5, 0, 1)))
    img[..., :3] = np.clip(c[None, None, :] * shade[..., None], 0, 1)
    img[..., 3] = np.clip(alpha, 0, 1)
    return img


def tex_for(col, seed):
    key = (tuple(np.round(col[:3], 3)), seed % 5)
    if key not in STATE["tex_cache"]:
        hexcol = "#%02x%02x%02x" % tuple(int(round(c * 255)) for c in col[:3])
        STATE["tex_cache"][key] = highlighter_texture(hexcol, 50 + seed)
    return STATE["tex_cache"][key]


def nice_step(vmax):
    raw = max(vmax, 1) / 7
    e = 10 ** np.floor(np.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * e:
            return m * e
    return 10 * e


def smooth_noise(rng, h, w, cell, blur=0):
    n = rng.random((h // cell + 2, w // cell + 2)).astype(np.float32)
    im = Image.fromarray((n * 255).astype("uint8")).resize((w, h), Image.BICUBIC)
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    return np.asarray(im, np.float32) / 255


_orig_background = g.make_background


def handmade_background(th):
    if th.get("texture") != "notebook":
        return _orig_background(th)
    W, H, HH = g.W, g.H, g.HEADER_H
    rng = np.random.default_rng(23)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    top, bot = g.hex255(P["paper_top"]), g.hex255(P["paper_bot"])
    img = top * (1 - (yy / H)[..., None]) + bot * (yy / H)[..., None]
    img += ((smooth_noise(rng, H, W, 3) - 0.5) * 7)[..., None]
    img += ((smooth_noise(rng, H, W, 60, blur=6) - 0.5) * 12)[..., None]
    fib = np.zeros((H, W), np.float32)
    for _ in range(900):
        x0, y0 = rng.uniform(0, W), rng.uniform(0, H)
        ang, L = rng.uniform(0, np.pi), rng.uniform(8, 34)
        t = np.linspace(0, 1, int(L))
        xs = np.clip((x0 + np.cos(ang) * L * t + np.sin(t * 3) * 1.5).astype(int), 0, W - 1)
        ys = np.clip((y0 + np.sin(ang) * L * t).astype(int), 0, H - 1)
        fib[ys, xs] += rng.uniform(0.4, 1.0)
    fib = np.asarray(Image.fromarray(np.clip(fib * 255, 0, 255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.6)),
                     np.float32) / 255
    img -= (fib * 10)[..., None]
    yr = yy - (xx - W / 2) * np.tan(TILT)
    rule = np.clip(1 - np.abs((yr - 20) % 59 - 0) / 1.25, 0, 1) * (yy > HH + 8)
    rule *= 0.75 + 0.25 * smooth_noise(rng, H, W, 40)
    img = img * (1 - 0.40 * rule[..., None]) + g.hex255(P["rules"]) * 0.40 * rule[..., None]
    xm = 34 + (yy - H / 2) * np.tan(TILT)
    margin = np.clip(1 - np.abs(xx - xm) / 1.3, 0, 1) * (yy > HH + 8)
    img = img * (1 - 0.42 * margin[..., None]) + g.hex255(P["margin"]) * 0.42 * margin[..., None]
    light = 1.03 - 0.07 * np.clip(np.hypot((xx - 120) / W, (yy - 300) / H) - 0.15, 0, 1)
    img *= light[..., None]
    fn = wob(31)
    edge = HH + fn(np.arange(W, dtype=float) * 0.5) * 5.0 + wob(32)(np.arange(W, dtype=float) * 3.1) * 1.6
    band = np.tile(g.hex255(P["header"]), (H, W, 1)).astype(np.float32)
    sw = np.zeros((H, W), np.float32)
    for k in range(9):
        yc = 14 + k * 44 + rng.uniform(-5, 5)
        hw = 30 + rng.uniform(-3, 4)
        ywav = yc + np.sin(xx / rng.uniform(180, 320) + rng.uniform(0, 6)) * 3
        sw += np.clip(1 - np.abs(yy - ywav) / hw, 0, 1) ** 0.6
    band *= (0.955 + 0.03 * np.clip(sw - 1, 0, 1) * -1 + 0.03 * smooth_noise(rng, H, W, 4))[..., None]
    band = band * (0.94 + 0.06 * (img / 255))
    inside = (yy <= edge[None, :])[..., None]
    img = np.where(inside, band, img)
    torn = np.clip(1 - np.abs(yy - edge[None, :] - 2.0) / 2.2, 0, 1) * (0.5 + 0.5 * smooth_noise(rng, H, W, 2))
    img = img * (1 - 0.35 * torn[..., None]) + 255 * 0.35 * torn[..., None]
    for k, (off, a_, wdt) in enumerate(((9, 0.85, 2.0), (17, 0.42, 1.3))):
        yl = edge + off + wob(40 + k)(np.arange(W, dtype=float) * 0.3) * 1.5
        line = np.clip(1 - np.abs(yy - yl[None, :]) / wdt, 0, 1) * a_
        line *= 0.8 + 0.2 * smooth_noise(rng, H, W, 30)
        img = img * (1 - line[..., None]) + g.hex255(INK) * line[..., None]
    img = washi(img, rng)
    return np.clip(img, 0, 255).astype(np.uint8)


def washi(img, rng):
    H, W = img.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    col = g.hex255(P["tape"])
    for (cx, cy, ang, L) in ((128, 78, np.radians(-27), 230), (W - 132, 70, np.radians(24), 220)):
        u = (xx - cx) * np.cos(ang) + (yy - cy) * np.sin(ang)
        v = -(xx - cx) * np.sin(ang) + (yy - cy) * np.cos(ang)
        tear = wob(int(cx))(v * 5.0) * 4.5
        inside = (np.abs(u) < L / 2 + tear) & (np.abs(v) < 26)
        weave = 0.5 + 0.25 * np.sin(u / 2.1) * np.sin(v / 2.3)
        stripe = (np.sin((u + v) / 5.5) > 0.55)
        a = inside * (0.40 + 0.08 * weave + 0.16 * stripe)
        edge = np.clip(1 - (26 - np.abs(v)) / 2.0, 0, 1) * inside
        a = np.clip(a + edge * 0.1, 0, 0.62)
        img = img * (1 - a[..., None]) + col * a[..., None]
        img += (inside * 6 * np.clip(1 - np.abs(v + 18) / 6, 0, 1))[..., None]
    return img


def paper_for_frame(i, n):
    bg = STATE["bg"]
    H, W = bg.shape[:2]
    z = 1.0 + PUSH_IN * (i / max(n - 1, 1))
    for L in STATE["lead_frames"]:
        z += NUDGE * np.exp(-((i - L) / NUDGE_W) ** 2)
    cw, ch = W / z, H / z
    cx, cy = W / 2, 1000.0
    x0 = float(np.clip(cx - cw / 2, 0, W - cw)); y0 = float(np.clip(cy - ch / 2, 0, H - ch))
    im = Image.fromarray(bg).resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
    out = np.asarray(im, np.int16) + STATE["grain"][(i // GRAIN_EVERY) % len(STATE["grain"])][..., None]
    return np.clip(out, 0, 255).astype(np.uint8)


_orig_scene = g.make_scene


def handmade_scene(*args, **kw):
    if kw.get("icon_path"):
        kw["icon_path"] = reink_icon(kw["icon_path"])
    fig, ax, year_txt, leader, art = _orig_scene(*args, **kw)
    STATE.update(fig=fig, ax=ax, art=art, year_txt=year_txt)
    STATE["bg"] = np.asarray(fig.images[0].get_array()).copy()
    rng = np.random.default_rng(5)
    STATE["grain"] = [rng.normal(0, 1.7, STATE["bg"].shape[:2]).astype(np.int16) for _ in range(4)]
    leader.set_color(INK); leader.set_alpha(0.30)
    for t in ax.texts:
        if t.get_position()[1] in (220, 306):
            t.set_path_effects(g.soft_shadow("#7a5c10", 0.30))
    STATE["rows"] = []
    for k, a in enumerate(art):
        bar = a["bar"]
        col = bar.get_facecolor()[:3]
        plain = a.get("stripe") is None
        row = dict(plain=plain, seed=k, fill_fn=boiled(1000 + k * 7), ink_fn=boiled(2000 + k * 7),
                   ink2_fn=boiled(3000 + k * 7), pill_fn=boiled(4000 + k * 7), rag=wob(5000 + k), cur_tex=None)
        if plain:
            bar.set_fill(False); bar.set_edgecolor("none")
            clip = Polygon(np.zeros((3, 2)), closed=True, fill=False, ec="none")
            ax.add_patch(clip)
            tex = ax.imshow(tex_for(col, k), extent=(0, 1, 1, 0), interpolation="bilinear")
            tex.set_clip_path(clip)
            row.update(clip=clip, tex=tex, cur_tex=tuple(np.round(col, 3)))
            for q in a["glow"]:
                q.set_facecolor(col)
        ink = Line2D([], [], color=INK, lw=2.5, alpha=0.88, solid_joinstyle="round", solid_capstyle="round")
        ink2 = Line2D([], [], color=INK, lw=1.4, alpha=0.42, solid_joinstyle="round", solid_capstyle="round")
        pill_ink = Line2D([], [], color=INK, lw=1.9, alpha=0.75, solid_joinstyle="round")
        arrow = Line2D([], [], color=INK, lw=4.0, solid_capstyle="round", solid_joinstyle="round", zorder=1150)
        arrow.set_visible(False)
        for ln in (ink, ink2, pill_ink, arrow):
            ax.add_line(ln)
        a["pill"].set_edgecolor("none")
        row.update(ink=ink, ink2=ink2, pill_ink=pill_ink, arrow=arrow)
        STATE["rows"].append(row)
    STATE["underline"] = [Line2D([], [], color=ACCENT, lw=5, alpha=0.9, solid_capstyle="round", zorder=999),
                          Line2D([], [], color=ACCENT, lw=3, alpha=0.5, solid_capstyle="round", zorder=999)]
    for ln in STATE["underline"]:
        ax.add_line(ln)
    probe = ax.text(0, 0, "2026", fontproperties=year_txt.get_fontproperties(), fontsize=year_txt.get_fontsize())
    STATE["year_w"] = probe.get_window_extent(fig.canvas.get_renderer()).width
    probe.remove()
    return fig, ax, year_txt, leader, art


def reink_icon(path):
    im = np.asarray(Image.open(path).convert("RGBA"), np.float32) / 255
    out = im.copy()
    out[..., :3] = np.array(g.hex_rgb(P.get("icon", INK)))[None, None, :]
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_icon_inked.png")
    Image.fromarray((out * 255).astype("uint8")).save(dst)
    return dst


_orig_draw = g.draw_frame


def handmade_draw(year_txt, leader, art, frame):
    _orig_draw(year_txt, leader, art, frame)
    year_txt.set_color(P["text"])
    if STATE["engage"] is None:
        nb_update(0, None)


def bar_progress(i, n, slot):
    p_in = ease((i - INTRO_DELAY - slot * INTRO_STAGGER) / INTRO_LEN)
    p_out = ease((n - 1 - i - (g.TOP_N - slot) * OUTRO_STAGGER) / OUTRO_LEN)
    return float(min(p_in, p_out))


def nb_update(i, frames):
    art = STATE["art"]
    n = len(frames) if frames is not None else None
    b = (i // BOIL_EVERY) % BOIL_VARIANTS
    if n:
        bg = paper_for_frame(i, n)
        STATE["fig"].images[0].set_data(bg)
        STATE["fig"].images[1].set_data(g.bottom_slab(bg))
    for j, (a, row) in enumerate(zip(art, STATE["rows"])):
        bar = a["bar"]
        on = bar.get_visible()
        for key in ("ink", "ink2", "pill_ink"):
            row[key].set_visible(on)
        if row["plain"]:
            row["tex"].set_visible(on)
        if not on:
            continue
        alpha = bar.get_alpha()
        alpha = 1.0 if alpha is None else alpha
        x, y, w, h = bar.get_x(), bar.get_y(), bar.get_width(), bar.get_height()
        z = bar.get_zorder()
        slot = int(np.clip(round((y + h / 2 - g.ROW0_YC) / g.ROW_H), 0, g.TOP_N + 1))
        p = bar_progress(i, n, slot) if n else 1.0
        tail = float(np.clip((p - 0.75) / 0.25, 0, 1))
        tail_items = [a["val"]] + ([a["logo"]] if a.get("logo") is not None else []) + ([a["rec"]] if a.get("rec") is not None else [])
        for q in tail_items:
            q.set_alpha((q.get_alpha() if q.get_alpha() is not None else 1.0) * tail)
            if tail < 0.05:
                q.set_visible(False)
        for q in a["glow"]:
            if q.get_visible():
                q.set_alpha((q.get_alpha() or 0) * p * 0.8)
        if row["plain"]:
            face = a["cur_col"][0] if a.get("cur_col") else bar.get_facecolor()[:3]
            key = tuple(np.round(face[:3], 3))
            if key != row["cur_tex"]:
                row["tex"].set_data(tex_for(face, row["seed"]))
                row["cur_tex"] = key
                for q in a["glow"]:
                    q.set_facecolor(face[:3])
            row["tex"].set_visible(p > 0.01)
            if p > 0.01:
                q = sketch(x, y, max(w * p, 12), h, 9, row["fill_fn"][b], AMP_FILL, ragged=row["rag"])
                row["clip"].set_xy(q)
                row["tex"].set_extent((x - 6, x - 6 + 900, y + h + 6, y - 6))
                row["tex"].set_alpha(alpha)
                row["tex"].set_zorder(z + 0.05)
        q1 = sketch(x, y, w, h, 9, row["ink_fn"][b], AMP_INK, overshoot=4)
        q2 = sketch(x, y, w, h, 9, row["ink2_fn"][b], AMP_INK2, overshoot=2)
        if p < 1:
            q1 = q1[: max(int(len(q1) * p), 0)]
            q2 = q2[: max(int(len(q2) * max(p - 0.15, 0) / 0.85), 0)]
        row["ink"].set_data(q1[:, 0], q1[:, 1]); row["ink2"].set_data(q2[:, 0], q2[:, 1])
        row["ink"].set_alpha(0.88 * alpha); row["ink2"].set_alpha(0.42 * alpha)
        row["ink"].set_zorder(z + 0.1); row["ink2"].set_zorder(z + 0.1)
        pl = a["pill"]
        qp = sketch(pl.get_x(), pl.get_y(), pl.get_width(), pl.get_height(), 16, row["pill_fn"][b], AMP_PILL, overshoot=3)
        row["pill_ink"].set_data(qp[:, 0], qp[:, 1])
        row["pill_ink"].set_alpha(0.75 * alpha)
        row["pill_ink"].set_zorder(pl.get_zorder() + 0.1)
        val = a["val"]
        val.set_color(SKIN["text"])
        if STATE["pops"] is not None and alpha > 0.99 and tail > 0.99:
            starts = STATE["pops"][j]
            k_ = np.searchsorted(starts, i, side="right") - 1
            if k_ >= 0 and i - starts[k_] < POP_LEN:
                t = (i - starts[k_]) / POP_LEN
                vx, vy = val.get_position()
                val.set_position((vx, vy - POP_HOP * np.sin(np.pi * t)))
                if t < 0.6:
                    val.set_color(ACCENT)
    yt = STATE["year_txt"]
    txt = yt.get_text()
    cache = STATE.setdefault("yw_cache", {})
    if txt not in cache:
        cache[txt] = yt.get_window_extent(yt.figure.canvas.get_renderer()).width
    yw = cache[txt] or STATE["year_w"]
    half = yw * 0.40
    xs = np.linspace(g.YEAR_X - half, g.YEAR_X + half, 24)
    for k, ln in enumerate(STATE["underline"]):
        fn = boiled(600 + k * 5)[b]
        base = g.YEAR_Y + 64 + k * 10 - (xs - xs[0]) * 0.025
        ln.set_data(xs + k * 10 * (1 - np.linspace(0, 1, 24)), base + fn(xs * 3) * 1.4)
    ev = STATE["events"]
    if ev is not None:
        for m, it in enumerate(ev.items):
            if it["ring"] is None:
                continue
            ring = it["ring"]
            loop = it.get("loop")
            if loop is None:
                loop = Line2D([], [], color=ACCENT, lw=3.6, solid_capstyle="round", solid_joinstyle="round", zorder=1050)
                STATE["ax"].add_line(loop)
                it["loop"] = loop
            on = ring.get_visible()
            loop.set_visible(on)
            ring.set_visible(False)
            if on:
                bar = it["art"][it["row"]]["bar"]
                pl = it["art"][it["row"]]["pill"]
                x_l = pl.get_x()
                cx, cy = (x_l + bar.get_x() + bar.get_width()) / 2, bar.get_y() + bar.get_height() / 2
                rx, ry = (bar.get_x() + bar.get_width() - x_l) / 2 + 18, bar.get_height() / 2 + 16
                rx = min(rx, (g.RIGHT_LIMIT - g.SAFE_X) / 2 - 4)
                drawn = float(np.clip((i - it["start"]) / 10, 0, 1))
                th = np.linspace(np.radians(200), np.radians(200 + 385 * drawn), max(int(90 * drawn), 2))
                rr = 1 + 0.03 * wob(900 + m)(th * 120) + 0.035 * (th - th[0]) / (2 * np.pi)
                loop.set_data(cx + rx * rr * np.cos(th), cy + ry * rr * np.sin(th) - 3 * np.sin(th * 0.5))
                loop.set_alpha(min(1.0, (ring.get_alpha() or 1) * 1.6))
    eng = STATE["engage"]
    if eng is not None:
        for j, tri in enumerate(eng.arrows):
            arrow = STATE["rows"][j]["arrow"]
            on = tri.get_visible()
            arrow.set_visible(on)
            tri.set_visible(False)
            if on:
                ax_, ay_ = tri.xy
                s = np.linspace(0, 1, 12)
                shaft_x = ax_ + 3 * np.sin(s * np.pi)
                shaft_y = ay_ + 22 - 44 * s
                head = [(ax_ - 13, ay_ - 8), (ax_ + 1, ay_ - 23), (ax_ + 14, ay_ - 7)]
                arrow.set_data(list(shaft_x) + [np.nan] + [h_[0] for h_ in head],
                               list(shaft_y) + [np.nan] + [h_[1] for h_ in head])
                arrow.set_alpha(tri.get_alpha() if tri.get_alpha() is not None else 1)
                arrow.set_zorder(tri.get_zorder())
        for fl in eng.flashes:
            fl.set_facecolor("#fff8dc")


_orig_engage = g.EngageLayer.__init__
_orig_engage_update = g.EngageLayer.update
_orig_event = g.EventLayer.__init__


def handmade_engage(self, ax, F, th, frames, art, *a, **kw):
    _orig_engage(self, ax, F, th, frames, art, *a, **kw)
    for t in self.q:
        t.set_color(P["title"]); t.set_path_effects([])
    self.panel.set_facecolor(P["header"]); self.panel.set_edgecolor(INK); self.panel.set_linewidth(3)
    self.panel.set_path_effects([])
    self.badge.set_facecolor(ACCENT); self.badge_t.set_color("#ffffff")
    STATE["engage"] = self
    STATE["lead_frames"] = [s for s, _ in self.lead_start]
    vals = np.array([fr[1] for fr in frames])
    step = nice_step(float(vals.max()))
    level = np.floor(vals / step + 1e-9)
    STATE["pops"] = [np.where(np.diff(level[:, j]) > 0)[0] + 1 for j in range(vals.shape[1])]


def handmade_engage_update(self, i):
    _orig_engage_update(self, i)
    nb_update(i, self.frames)


def handmade_event(self, ax, F, th, *a, **kw):
    _orig_event(self, ax, F, th, *a, **kw)
    for it in self.items:
        it["card"].set_path_effects([])
        it["card"].set_edgecolor(INK); it["card"].set_linewidth(2)
        txt_col = "#1a1a1a" if g.rel_lum(g.hex_rgb(ACCENT)) > 0.35 else "#ffffff"
        it["tag"].set_color(txt_col); it["body"].set_color(txt_col)
    STATE["events"] = self


def main():
    for th in g.THEMES.values():
        th.update(SKIN)
    g.ensure_contrast = lambda col, bg, target=3.0: tuple(c + (1 - c) * 0.04 for c in col)
    g.make_background = handmade_background
    g.make_scene = handmade_scene
    g.draw_frame = handmade_draw
    g.EngageLayer.__init__ = handmade_engage
    g.EngageLayer.update = handmade_engage_update
    g.EventLayer.__init__ = handmade_event
    g.main()
    shrink_if_large()


def shrink_if_large(limit_mb=24.0):
    import subprocess
    outs = [a for a in sys.argv[1:] if a.lower().endswith(".mp4")]
    if "--preview" in sys.argv or not outs or not os.path.exists(outs[-1]):
        return
    dst = outs[-1]
    if os.path.getsize(dst) / 1e6 <= limit_mb:
        return
    tmp = dst[:-4] + ".crf22.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", dst, "-c:v", "libx264", "-preset", "medium",
                    "-crf", "22", "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, dst)
    print(f"re-encoded at CRF 22: {os.path.getsize(dst) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
