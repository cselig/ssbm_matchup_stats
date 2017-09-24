import sqlite3


def create_tables(conn, c):
	c.execute('''CREATE TABLE players (
		pid INTEGER PRIMARY KEY NOT NULL,
		tag TEXT,
		rank INTEGER)''')

	"""this is the schema I would want to use if I had all the data"""
	# # in sets and games, winner is pid of winning player
	# c.execute('''CREATE TABLE sets (
	# 	set_id INTEGER PRIMARY KEY NOT NULL,
	# 	sdate DATE,
	# 	tourney TEXT,
	# 	set_name TEXT,
	# 	p1 INTEGER,
	# 	p2 INTEGER,
	# 	winner INTEGER)''')

	# c.execute('''CREATE TABLE games (
	# 	set_id INTEGER,
	# 	game_num INTEGER,
	# 	stage TEXT,
	# 	p1char TEXT,
	# 	p2char TEXT,
	# 	winner INTEGER,
	# 	stock_diff TEXT,
	# 	FOREIGN KEY (set_id) REFERENCES sets(set_id))''')

	"""alternative schema just for games data"""


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