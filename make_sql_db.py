import sqlite3
import pickle


def create_tables(conn, c):
	c.execute('''CREATE TABLE players (
		pid INTEGER PRIMARY KEY NOT NULL,
		tag TEXT,
		rank INTEGER)''')

	c.execute('''CREATE TABLE games (
		p1id INTEGER,
		p2id INTEGER,
		p1char TEXT,
		p2char TEXT,
		winner INTEGER)''')

	conn.commit()


def create_tables_in_memory():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    create_tables(conn, c)
    return conn, c


def add_data(conn, c):
	pass


def test_queries(conn, c):
	pass


def test():
	conn, c = create_tables_in_memory()
	add_data(conn, c)
	test_queries(conn, c)


if __name__ == '__main__':
	test()