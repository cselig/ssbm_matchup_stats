import sqlite3
import pandas as pd


conn = sqlite3.connect('../db/ssbm.db')
# ['Kongo Jungle', 'Rainbow Cruise', '??', 'Mute City', 'Brinstar', 'Corneria', 'Green Greens']

legal_stages = ['Final Destination', 'Pokemon Stadium', 'Battlefield', 'Dreamland', "Yoshi's Story", 'Fountain of Dreams']

def query(char1, char2):
    c = conn.cursor()

    c.execute('''
        SELECT sum(case when winner_char = ? then 1 else 0 end) 
            * 1.0 / sum(1), sum(1) as count
        from(
            select *, 
                (case when games.winner = p1_tag then p1_char 
                when games.winner = p2_tag then p2_char end)
                as winner_char
            from sets join games using(setid)
            where p1_char = ? and p2_char = ? or 
                p1_char = ? and p2_char = ?)''', (char1, char1, char2, char2, char1))

    # print(str(c.fetchone()))
    return c

def query_chars_by_stage(char1, char2):
    c = conn.cursor()

    c.execute('''
        SELECT 
            stage, 
            (sum(case when winner_char = ? then 1 else 0 end) * 1.0 / sum(1) * 100) as percent_win, 
            sum(1) as total_games
        from(
            select 
                *, 
                (case when games.winner = p1_tag then p1_char 
                when games.winner = p2_tag then p2_char end) as winner_char
            from sets join games using(setid)
            where (p1_char = ? and p2_char = ? or 
                p1_char = ? and p2_char = ?)
            ) 
            where stage in ('Final Destination', 'Pokemon Stadium', 'Battlefield', 'Dreamland', "Yoshi's Story", 'Fountain of Dreams')
            group by stage
            order by percent_win desc''', 
            (char1, char1, char2, char2, char1))

    return c


# def query_chars_and_stage(char1, char2, stage):
#     c = conn.cursor()

#     c.execute('''SELECT *
#         from(
#             select *
#             from sets join games using(setid)
#             where p1_char = ? and p2_char = ? or 
#                 p1_char = ? and p2_char = ?
#             )''',
#         (char1, char2, char2, char1))

#     return c


if __name__ == '__main__':
    char1 = input('Enter first character: ')
    char2 = input('Enter second character: ')

    # c = query_test()
    
    # for row in c.fetchall():
    #     print(row)

    for row in query_chars_by_stage(char1, char2).fetchall():
        print(row)

    conn.close()




# c = query(char1, char2)

# df = pd.read_sql_query("""
#         SELECT * 
#         from(
#             select *, 
#                 (case when games.winner = p1_tag then p1_char 
#                 when games.winner = p2_tag then p2_char end)
#                 as winner_char
#             from sets join games using(setid)
#             where (p1_char = 'Marth' and p2_char = 'Fox' or 
#                 p1_char = 'Fox' and p2_char = 'Marth')
#                 and stage = 'Final Destination')
#         where winner_char = 'Marth'""", conn)
        

# print(df)


# c.execute('''
#     SELECT 
#         sum(case when winner = 'Armada' then 1 else 0 end) 
#         * 1.0 /
#         count(*)
#     from 
#         (select * 
#         from sets
#         where p1_tag = 'Armada' or p2_tag = 'Armada')
#     ''')

# c.execute('''
#     SELECT sum(case when winner_char = 'Marth' then 1 else 0 end) 
#         * 1.0 / sum(1) 
#     from(
#         select *, 
#             case when games.winner = p1_tag then p1_char 
#             when games.winner = p2_tag then p2_chat end 
#             as winner_char
#         from sets join games using(setid)
#         where p1_char = 'Marth' and p2_chat = 'Fox' or 
#             p1_char = 'Fox' and p2_chat = 'Marth' and 
#             stage = 'Battlefield')
#     ''')