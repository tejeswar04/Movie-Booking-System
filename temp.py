import sqlite3

with sqlite3.connect('database.db') as con:
    cur=con.cursor()
    #con.execute("DROP TABLE bookings")
    #con.execute("DROP TRIGGER prevent_duplicate_booking")
    cur.execute("""select name from sqlite_master where type = 'trigger'""")
    print(cur.fetchall())
con.close()