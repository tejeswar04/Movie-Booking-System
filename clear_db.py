import sqlite3

with sqlite3.connect('database.db') as con:
    #con.execute("""Drop Table movies_add""")
    cur = con.cursor()
    #cur.execute("""select name from sqlite_master where type = 'trigger'""")
    #print(cur.fetchall())
    #cur.execute("""Drop table movies_add""")
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("Dumb and Dumber", 124, "Comedy"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("Mean Girls", 100, "Comedy"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("Andaz Apna Apna", 160, "Comedy"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("Interstellar", 170, "Action"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("Nobody", 130, "Action"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("Inception", 150, "Action"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("After We Collided", 100, "Romance"))
    cur.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)", ("The Notebook", 105, "Romance"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(1, "15:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(1, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(1, "21:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(2, "13:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(2, "15:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(2, "17:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(2, "19:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(3, "15:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(3, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(3, "21:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(4, "10:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(4, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(4, "22:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(5, "15:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(5, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(5, "21:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(6, "10:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(6, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(6, "22:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(7, "15:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(7, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(7, "21:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(8, "15:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(8, "18:00"))
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(8, "21:00"))
    cur.execute("INSERT INTO theaters VALUES (?, ?)",("INOX","Manipal"))
    cur.execute("INSERT INTO theaters VALUES (?, ?)",("Bharat Cinemas","Manipal"))
    cur.execute("INSERT INTO theaters VALUES (?, ?)",("PVR","Manipal"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","A","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","A","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","A","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","A","4"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","B","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","B","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","B","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","C","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","C","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","C","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","C","4"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("INOX","C","5"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","A","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","A","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","A","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","B","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","B","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","B","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","C","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","C","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","C","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","D","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","D","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("PVR","D","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","A","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","A","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","B","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","B","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","C","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","C","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","C","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","D","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","D","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Bharat Cinemas","D","3"))
    '''
    cur.execute("INSERT INTO showtimes (movie_id, time) VALUES (?, ?)",(1, "03:00"))
    cur.execute("INSERT INTO theaters VALUES (?, ?)",("Citylight","Mahim"))
    cur.execute("INSERT INTO theaters VALUES (?, ?)",("Starcity","Mahim"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","A","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","A","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","A","3"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","A","4"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","B","1"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","B","2"))
    cur.execute("INSERT INTO seats VALUES (?, ?, ?)",("Citylight","B","3"))
    cur.execute("""CREATE TABLE IF NOT EXISTS showtimes (
                        movie_id integer NOT NULL,
                        time text NOT NULL,
                        FOREIGN KEY (movie_id)
                            REFERENCES movies (id)
                                ON UPDATE SET NULL
                                ON DELETE SET NULL
                        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS theaters (
                        t_name text PRIMARY KEY,
                        location text
                        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS seats (
                        t_name text,
                        row text,
                        seat text,
                        FOREIGN KEY (t_name)
                            REFERENCES theaters (t_name)
                                ON UPDATE SET NULL
                                ON DELETE SET NULL
                        );""")
    cur.execute("""CREATE TRIGGER IF NOT EXISTS prevent_duplicate_booking
                       BEFORE INSERT ON bookings
                       FOR EACH ROW
                       BEGIN
                           SELECT RAISE(ABORT, 'Seat already booked for this movie and time')
                           FROM bookings
                           WHERE movie_id = NEW.movie_id
                           AND date = NEW.date
                           AND time = NEW.time
                           AND row = NEW.row
                           AND seat = NEW.seat;
                       END;
                    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS movies_add(
                    movie_name text Primary Key NOT NULL,
                    d DATE NOT NULL
                    );""")
    '''
con.close()