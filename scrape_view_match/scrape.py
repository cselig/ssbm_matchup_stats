# Scrapes sets and games from tafostats. Doesn't get set date or tournament. 

import requests
from bs4 import BeautifulSoup
import sqlite3

URL = 'http://t5dev.smash4tips.com/pages/ViewMatch.cfm'


def create_tables(conn, c):
    c.execute('DROP TABLE sets')
    c.execute('DROP TABLE games')
    c.execute('''CREATE TABLE sets (
         setid TEXT PRIMARY KEY NOT NULL,
         p1_tag TEXT,
         p2_tag TEXT,
         winner TEXT)''')

    c.execute('''CREATE TABLE games (
        setid TEXT,
        game INTEGER,
        stage TEXT,
        p1_char TEXT,
        p2_chat TEXT,
        winner TEXT,
        stock_diff INTEGER,
        FOREIGN KEY (setid) REFERENCES sets(setid))''')

    conn.commit()


def get_html(setid):
    return requests.post(URL, {'setid': str(setid)})


def parse_html(html, setid):
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.table
    match = [str(setid)]
    games = []

    # needed to determine set winner
    p1wins = 0
    p2wins = 0

    # get header
    for i, entry in enumerate(soup.find_all('th')):
        if i in [2, 3]:
            match.append(str(entry.text))

    # get games
    for entry in soup.find_all('tr')[1:]:
        game = [str(setid)]
        for item in entry.find_all('td'):
            game.append(str(item.text))
        if game[5] == match[1]: 
            p1wins += 1
        elif game[5] == match[2]:
            p2wins += 1
        if game[-1] == '??':
            game[-1] = None
        games.append(game)
        
    # determine winner of match
    if p1wins > p2wins:
        match.append(match[1])
    elif p2wins > p1wins:
        match.append(match[2])
    else:
        match.append(None)

    return match, games


def write_out(match, games, c):
    print(match)
    for g in games:
        print('\t' + str(g))
    c.execute('INSERT INTO sets VALUES (?,?,?,?)', match)
    c.executemany('INSERT INTO games VALUES (?,?,?,?,?,?,?)', games)


if __name__ == '__main__':
    conn = sqlite3.connect('ssbm.db')
    c = conn.cursor()
    create_tables(conn, c)

    for setid in range(0, 0): # 2227 is lowest null set
        r = get_html(setid)
        if 'Error Occurred While Processing Request' not in r.text:
            match, games = parse_html(r.text, setid)
            write_out(match, games, c)
    conn.commit()

    test_queries(conn, c)