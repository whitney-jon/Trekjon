# Calendar-year trophy wins 1992-2026 (English clubs). Type codes: L league, F FA Cup, C League Cup,
# S Community Shield, E European Cup/CL, U UEFA Cup/Europa, K Conference League, W Cup Winners' Cup,
# P UEFA Super Cup, I Intercontinental/Club World Cup, O other (Intertoto)
WINS = []
def add(t, rows):
    for y, c in rows: WINS.append((y, c, t))
# league title, year the season ended
add('L', [(1992,'Leeds United'),(1993,'Manchester United'),(1994,'Manchester United'),(1995,'Blackburn Rovers'),(1996,'Manchester United'),
 (1997,'Manchester United'),(1998,'Arsenal'),(1999,'Manchester United'),(2000,'Manchester United'),(2001,'Manchester United'),(2002,'Arsenal'),
 (2003,'Manchester United'),(2004,'Arsenal'),(2005,'Chelsea'),(2006,'Chelsea'),(2007,'Manchester United'),(2008,'Manchester United'),
 (2009,'Manchester United'),(2010,'Chelsea'),(2011,'Manchester United'),(2012,'Manchester City'),(2013,'Manchester United'),(2014,'Manchester City'),
 (2015,'Chelsea'),(2016,'Leicester City'),(2017,'Chelsea'),(2018,'Manchester City'),(2019,'Manchester City'),(2020,'Liverpool'),
 (2021,'Manchester City'),(2022,'Manchester City'),(2023,'Manchester City'),(2024,'Manchester City'),(2025,'Liverpool'),(2026,'Arsenal')])
add('F', [(1992,'Liverpool'),(1993,'Arsenal'),(1994,'Manchester United'),(1995,'Everton'),(1996,'Manchester United'),(1997,'Chelsea'),(1998,'Arsenal'),
 (1999,'Manchester United'),(2000,'Chelsea'),(2001,'Liverpool'),(2002,'Arsenal'),(2003,'Arsenal'),(2004,'Manchester United'),(2005,'Arsenal'),
 (2006,'Liverpool'),(2007,'Chelsea'),(2008,'Portsmouth'),(2009,'Chelsea'),(2010,'Chelsea'),(2011,'Manchester City'),(2012,'Chelsea'),
 (2013,'Wigan Athletic'),(2014,'Arsenal'),(2015,'Arsenal'),(2016,'Manchester United'),(2017,'Arsenal'),(2018,'Chelsea'),(2019,'Manchester City'),
 (2020,'Arsenal'),(2021,'Leicester City'),(2022,'Liverpool'),(2023,'Manchester City'),(2024,'Manchester United'),(2025,'Crystal Palace'),(2026,'Manchester City')])
add('C', [(1992,'Manchester United'),(1993,'Arsenal'),(1994,'Aston Villa'),(1995,'Liverpool'),(1996,'Aston Villa'),(1997,'Leicester City'),(1998,'Chelsea'),
 (1999,'Tottenham Hotspur'),(2000,'Leicester City'),(2001,'Liverpool'),(2002,'Blackburn Rovers'),(2003,'Liverpool'),(2004,'Middlesbrough'),(2005,'Chelsea'),
 (2006,'Manchester United'),(2007,'Chelsea'),(2008,'Tottenham Hotspur'),(2009,'Manchester United'),(2010,'Manchester United'),(2011,'Birmingham City'),
 (2012,'Liverpool'),(2013,'Swansea City'),(2014,'Manchester City'),(2015,'Chelsea'),(2016,'Manchester City'),(2017,'Manchester United'),
 (2018,'Manchester City'),(2019,'Manchester City'),(2020,'Manchester City'),(2021,'Manchester City'),(2022,'Liverpool'),(2023,'Manchester United'),
 (2024,'Liverpool'),(2025,'Newcastle United'),(2026,'Manchester City')])
add('S', [(1992,'Leeds United'),(1993,'Manchester United'),(1994,'Manchester United'),(1995,'Everton'),(1996,'Manchester United'),(1997,'Manchester United'),
 (1998,'Arsenal'),(1999,'Arsenal'),(2000,'Chelsea'),(2001,'Liverpool'),(2002,'Arsenal'),(2003,'Manchester United'),(2004,'Arsenal'),(2005,'Chelsea'),
 (2006,'Liverpool'),(2007,'Manchester United'),(2008,'Manchester United'),(2009,'Chelsea'),(2010,'Manchester United'),(2011,'Manchester United'),
 (2012,'Manchester City'),(2013,'Manchester United'),(2014,'Arsenal'),(2015,'Arsenal'),(2016,'Manchester United'),(2017,'Arsenal'),(2018,'Manchester City'),
 (2019,'Manchester City'),(2020,'Arsenal'),(2021,'Leicester City'),(2022,'Liverpool'),(2023,'Arsenal'),(2024,'Manchester City'),(2025,'Crystal Palace'),(2026,'Arsenal')])
add('E', [(1999,'Manchester United'),(2005,'Liverpool'),(2008,'Manchester United'),(2012,'Chelsea'),(2019,'Liverpool'),(2021,'Chelsea'),(2023,'Manchester City')])
add('U', [(2001,'Liverpool'),(2013,'Chelsea'),(2017,'Manchester United'),(2019,'Chelsea'),(2025,'Tottenham Hotspur'),(2026,'Aston Villa')])
add('K', [(2023,'West Ham United'),(2025,'Chelsea'),(2026,'Crystal Palace')])
add('W', [(1994,'Arsenal'),(1998,'Chelsea')])
add('P', [(1998,'Chelsea'),(2001,'Liverpool'),(2005,'Liverpool'),(2019,'Liverpool'),(2021,'Chelsea'),(2023,'Manchester City')])
add('I', [(1999,'Manchester United'),(2008,'Manchester United'),(2019,'Liverpool'),(2021,'Chelsea'),(2023,'Manchester City'),(2025,'Chelsea')])
add('O', [(1999,'West Ham United'),(2001,'Aston Villa'),(2002,'Fulham'),(2006,'Newcastle United')])
# all-time totals (Wikipedia, Aug 2026, incl. 'Other' and the 2026 Community Shield)
TOTAL = {'Liverpool':70,'Manchester United':68,'Arsenal':51,'Manchester City':38,'Chelsea':36,'Tottenham Hotspur':27,'Aston Villa':26,'Everton':24,
 'Newcastle United':15,'Nottingham Forest':13,'Wolverhampton Wanderers':13,'Blackburn Rovers':12,'Sunderland':10,'Sheffield Wednesday':10,
 'Leeds United':9,'West Bromwich Albion':9,'West Ham United':7,'Leicester City':7,'Sheffield United':6,'Huddersfield Town':5,'Portsmouth':5,
 'Burnley':5,'Bolton Wanderers':5}
