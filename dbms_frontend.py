from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import datetime
import dbms_backend
import custom_widgets

class User():
    def __init__(self, root, logo,username):
        self.root = root
        self.logo = logo
        self.username=username
        title = Label(self.root, text="CINE APP", font=("Helvetica", 40, "bold"), fg="red", bg="#46464a", image=self.logo, compound='left').pack()
        
        #main navigation buttons
        self.movies = custom_widgets.MainButton(self.root, text="View Movies", command = self.view_movies_UI)
        self.movies.place(x=30, y=110)

        self.add_booking = custom_widgets.MainButton(self.root, text="Add Booking", command = self.add_booking_UI)
        self.add_booking.place(x=185, y=110)

        self.view_bookings = custom_widgets.MainButton(self.root, text="View Booking", command = self.view_bookings_UI)
        self.view_bookings.place(x=340,y=110)

        #main frame for all widgets
        self.main_frame = Frame(self.root, background="#46464a", width=1000, height= 600)
        self.main_frame.place(x=0,y=160)

        bravo_dbms_backend.create_tables()

        self.error_msg = """ERROR Check if something is empty"""

    #to check if widgets are empty
    def check_widgets(self, *args):
        value = False
        for widget in args:
            if widget == "":
                value = False
                break
            else:
                value = True
        return value

    #to reset the buttons background
    def button_background(self):
        self.movies.config(bg="#46464a", relief="raised")
        self.add_booking.config(bg="#46464a", relief="raised")

    #to reset the main frame
    def delete_widgets(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    #view movies
    def view_movies_UI(self):
        self.button_background()
        self.movies.config(bg="#2c2c2e", relief = "sunken")
        self.delete_widgets()

        #main label
        lbl_all_movies = Label(self.main_frame, text="All movies", font=("Helvetica", 13), bg="#46464a", fg="red")
        lbl_all_movies.place(x=50, y=0)
        movies_frame = Frame(self.main_frame, bg="white")
        movies_frame.place(x=50, y= 30)

        tree_scroll = Scrollbar(movies_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        #tree view table for database
        movie_tree = ttk.Treeview(movies_frame, column=("#1", "#2", "#3", "#4"), show='headings', yscrollcommand=tree_scroll.set)
        #table customisation
        tree_style = ttk.Style()
        tree_style.theme_use("clam")
        tree_style.configure("Treeview", background="#46464a", fieldbackground="#46464a", foreground="white")
        tree_style.map('Treeview', background=[("selected", "#2c2c2e")])

        tree_scroll.config(command=movie_tree.yview)
        #columns and headins
        movie_tree.column("#1", anchor=CENTER, width=60)
        movie_tree.column("#2", anchor=CENTER, width=120)
        movie_tree.column("#3", anchor=CENTER, width=80)
        movie_tree.column("#4", anchor=CENTER, width=110)
        movie_tree.heading("#1", text="ID")
        movie_tree.heading("#2", text="Name")
        movie_tree.heading("#3", text="Run Time")
        movie_tree.heading("#4", text="Genre/s")
        movie_tree.pack()        
        
        #function for display button
        def view_movies():
            for row in movie_tree.get_children():
                movie_tree.delete(row)
            order = box_order_movie.get()
            rows = bravo_dbms_backend.get_all_movies(order)
            print(rows)
            for row in rows:
                movie_tree.insert("", END, values=row)

        #order movies option
        lbl_order_movie = custom_widgets.WhiteLabel(self.main_frame, text="Order by:")
        lbl_order_movie.place(x=390, y=0)
        movie_columns = ["movie_id", "name", "run_time", "genre"]
        box_order_movie = ttk.Combobox(self.main_frame, values=movie_columns)
        box_order_movie.place(x=460, y=0)

        #display data button
        display_movies = custom_widgets.OrangeButton(self.main_frame, text="Display Movies", command=view_movies)
        display_movies.place(x=50, y=290)

    #add bookings
    def add_booking_UI(self):
        self.button_background()
        self.add_booking.config(bg="#2c2c2e", relief = "sunken")
        self.delete_widgets()

        #choosing movie name
        lbl_movie_name = custom_widgets.WhiteLabel(self.main_frame, text="Movie Name:")
        lbl_movie_name.place(x=30, y=5)
        movie_names = []
        movies = bravo_dbms_backend.get_all_movies()
        for movie in movies:
                movie_names.append(movie[1])

        #added this function
        def pick_times(event):
            box_movie_time.config(value=bravo_dbms_backend.get_showtimes(box_movie_name.get()))

        box_movie_name = ttk.Combobox(self.main_frame, values=movie_names)
        box_movie_name.place(x=30, y=30)
        box_movie_name.bind("<<ComboboxSelected>>",pick_times)

        #choosing a date
        def output_date():
            lbl_date = Label(self.main_frame, text=cal_movie_date.get_date(), font=("Helvetica", 13), bg="#46464a", fg="red")
            lbl_date.place(x=125, y=280)
        lbl_movie_date = custom_widgets.WhiteLabel(self.main_frame, text="Choose Date:")
        lbl_movie_date.place(x=30, y=60)
        current_date = datetime.datetime.now()
        cal_movie_date = Calendar(self.main_frame, selectmode="day", year=current_date.year, month=current_date.month, )
        cal_movie_date.place(x=30, y=85)
        enter_date_button = custom_widgets.OrangeButton(self.main_frame, text="Select Date", command=output_date)
        enter_date_button.place(x=30, y=280)

        #choosing a time
        lbl_movie_time = custom_widgets.WhiteLabel(self.main_frame, text="Choose Time:")
        lbl_movie_time.place(x=30, y=310)
        times = [" "]
        '''
        times = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00",
                 "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
                 "20:00", "21:00", "22:00", "23:00"]'''
        box_movie_time = ttk.Combobox(self.main_frame, values=times)
        box_movie_time.place(x=30, y=335)

        #added this function
        def pick_row(event):
            box_rows.config(value=bravo_dbms_backend.get_rows(box_theater.get()))

        #choosing a theater
        lbl_theater = custom_widgets.WhiteLabel(self.main_frame, text="Choose Theater:")
        lbl_theater.place(x=215, y=310)
        #rows = ["Citylight", "Starcity"]
        theaters = bravo_dbms_backend.get_theaters()
        box_theater = ttk.Combobox(self.main_frame, values=theaters)
        box_theater.place(x=215, y=335)
        box_theater.bind("<<ComboboxSelected>>",pick_row)

        def pick_seat(event):
            box_seats.config(value=bravo_dbms_backend.get_seats(box_theater.get(), box_rows.get()))

        #choosing a row
        lbl_rows = custom_widgets.WhiteLabel(self.main_frame, text="Choose Row:")
        lbl_rows.place(x=30, y=365)
        rows = [" "]
        #rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        box_rows = ttk.Combobox(self.main_frame, values=rows)
        box_rows.place(x=30, y=390)
        box_rows.bind("<<ComboboxSelected>>",pick_seat)

        #choosing a seat
        lbl_seats = custom_widgets.WhiteLabel(self.main_frame, text="Choose Seat:")
        lbl_seats.place(x=215, y=365)
        seats = [" "]
        #seats = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        box_seats = ttk.Combobox(self.main_frame, values=seats)
        box_seats.place(x=215, y=390)

        #choosing the pricing
        radio_group = StringVar()
        adult_txt="""Adult
        \u20B9 300"""
        child_txt="""Child
        \u20B9 150"""
        Student_txt="""Student
        \u20B9 200"""
        radio_adult = custom_widgets.PriceRadiobutton(self.main_frame, text=adult_txt, variable=radio_group, value="300")
        radio_child = custom_widgets.PriceRadiobutton(self.main_frame, text=child_txt, variable=radio_group, value="150")
        radio_student = custom_widgets.PriceRadiobutton(self.main_frame, text=Student_txt, variable=radio_group, value="200")
        radio_adult.place(x=30, y=430)
        radio_child.place(x=140, y=430)
        radio_student.place(x=250, y=430)
        radio_group.set(None)

        #function for submit and clear button
        def submit_booking():
            movie = box_movie_name.get()
            date = cal_movie_date.get_date()
            time = box_movie_time.get()
            row = box_rows.get()
            seat = box_seats.get()
            price = radio_group.get()
            check_widgets = self.check_widgets(movie, date, time, row, seat, price)
            if check_widgets:
                bravo_dbms_backend.insert_booking(movie, date, time, row, seat, price, self.username, box_theater.get())
                clear_booking()
            else:
                lbl_error = Label(self.main_frame, text=self.error_msg, fg="red", bg="#46464a", font=("Ariel", 10))
                lbl_error.place(x=160, y=489)
                lbl_error.after(8000, lbl_error.destroy)

        def clear_booking():
            box_movie_name.set(" ")
            cal_movie_date.selection_clear()
            box_movie_time.set(" ")
            box_rows.set(" ")
            box_seats.set(" ")
            radio_group.set(None)

        #buttons
        submit_button = custom_widgets.OrangeButton(self.main_frame, text="Submit", command=submit_booking)
        submit_button.place(x=30, y=489)
        clear_button = Button(self.main_frame, text="Clear", bg="grey", fg="white", padx=5, command=clear_booking)
        clear_button.place(x=105, y=489)

    def view_bookings_UI(self):
        self.button_background()
        self.movies.config(bg="#2c2c2e", relief = "sunken")
        self.delete_widgets()

        #main label
        lbl_all_movies = Label(self.main_frame, text="Your Bookings", font=("Helvetica", 13), bg="#46464a", fg="red")
        lbl_all_movies.place(x=220, y=0)
        movies_frame = Frame(self.main_frame, bg="white")
        movies_frame.place(x=0, y= 30)

        #tree_scroll = Scrollbar(movies_frame)
        #tree_scroll.pack(side=RIGHT, fill=Y)
        #tree view table for database
        movie_tree = ttk.Treeview(movies_frame, column=("#1", "#2", "#3", "#4", "#5","#6","#7","#8","#9","#10"), show='headings')
        #table customisation
        tree_style = ttk.Style()
        tree_style.theme_use("clam")
        tree_style.configure("Treeview", background="#46464a", fieldbackground="#46464a", foreground="white")
        tree_style.map('Treeview', background=[("selected", "#2c2c2e")])

        #tree_scroll.config(command=movie_tree.yview)
        #columns and headins
        movie_tree.column("#1", anchor=CENTER, width=60)
        movie_tree.column("#2", anchor=CENTER, width=60)
        movie_tree.column("#3", anchor=CENTER, width=60)
        movie_tree.column("#4", anchor=CENTER, width=60)
        movie_tree.column("#5", anchor=CENTER, width=60)
        movie_tree.column("#6", anchor=CENTER, width=60)
        movie_tree.column("#7", anchor=CENTER, width=60)
        movie_tree.column("#8", anchor=CENTER, width=60)
        movie_tree.column("#9", anchor=CENTER, width=60)
        movie_tree.column("#10", anchor=CENTER, width=60)
        movie_tree.heading("#1", text="Booking_ID")
        movie_tree.heading("#2", text="Username")
        movie_tree.heading("#3", text="movie_id")
        movie_tree.heading("#4", text="movie_name")
        movie_tree.heading("#5", text="Date")
        movie_tree.heading("#6", text="time")
        movie_tree.heading("#7", text="row")
        movie_tree.heading("#8", text="seat")
        movie_tree.heading("#9", text="Price")    
        movie_tree.heading("#10", text="Theater")     
        movie_tree.pack()        
 
        #function for display button
        def view_bookings():
            for row in movie_tree.get_children():
                movie_tree.delete(row)
            rows = bravo_dbms_backend.get_your_bookings(self.username)
            print(rows)
            for row in rows:
                movie_tree.insert("", END, values=row)
        """
        movie_columns = ["Booking_ID", "Username", "movie_id", "Date", "time", "row", "seat", "Price"]
        box_order_movie = ttk.Combobox(self.main_frame, values=movie_columns)
        box_order_movie.place(x=460, y=0)
        """
        #display data button
        display_movies = custom_widgets.OrangeButton(self.main_frame, text="Display Your Bookings", command=view_bookings)
        display_movies.place(x=50, y=290)

#============================================================================
class Admin():
    def __init__(self, root, logo, username):
        self.root = root
        self.logo = logo
        self.username=username

        title = Label(self.root, text="CINE APP", font=("Helvetica", 40, "bold"), fg="red", bg="#46464a", image=self.logo, compound='left').pack()

        self.movies = custom_widgets.MainButton(self.root, text="View Movies", command = self.view_movies_UI)
        self.movies.place(x=30, y=110)
        
        #main navigation buttons
        self.add_movie = custom_widgets.MainButton(self.root, text="Add Movie", command = self.add_movie_UI)
        self.add_movie.place(x=185, y=110)

        self.bookings = custom_widgets.MainButton(self.root, text="View Bookings", command = self.view_bookings_UI)
        self.bookings.place(x=320, y=110)

        self.add_booking = custom_widgets.MainButton(self.root, text="Add Booking", command = self.add_booking_UI)
        #self.add_booking.place(x=185, y=110)

        self.add_booking.place(x=490, y=110)

        self.query=custom_widgets.MainButton(self.root, text="Run Query", command=self.run_query_UI)
        self.query.place(x=640, y=110)

        self.main_frame = Frame(self.root, background="#46464a", width=1000, height= 600)
        self.main_frame.place(x=0,y=160)

    def run_query_UI(self):   
        def run_q():
            booking_id = txt_booking_id.get()
            output=bravo_dbms_backend.get_query(booking_id)
            txt_booking_id.delete(0, END) 
        self.delete_widgets()       
        lbl_booking_id = custom_widgets.WhiteLabel(self.main_frame,  text="Query: ")
        lbl_booking_id.place(x=0, y=30)
        #lbl_booking_id.grid(row=0, column=0)
        txt_booking_id = custom_widgets.GreyEntry(self.main_frame)
        txt_booking_id.place(x=0, y=50)
        #txt_booking_id.grid(row=0, column=1)
        remove_booking_button = custom_widgets.OrangeButton(self.main_frame, text="Query to Run", command=run_q)
        remove_booking_button.place(x=225, y=50)
        #remove_booking_button.grid(row=0, column=2) 

    def check_widgets(self, *args):
        value = False
        for widget in args:
            if widget == "":
                value = False
                break
            else:
                value = True
        return value

    #to reset the buttons background
    def button_background(self):
        self.movies.config(bg="#46464a", relief="raised")
        self.add_booking.config(bg="#46464a", relief="raised")

    #to reset the main frame
    def delete_widgets(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def add_booking_UI(self):
        self.button_background()
        self.add_booking.config(bg="#2c2c2e", relief = "sunken")
        self.delete_widgets()

        #choosing movie name
        lbl_movie_name = custom_widgets.WhiteLabel(self.main_frame, text="Movie Name:")
        lbl_movie_name.place(x=30, y=5)
        movie_names = []
        movies = bravo_dbms_backend.get_all_movies()
        for movie in movies:
                movie_names.append(movie[1])

        #added this function
        def pick_times(event):
            box_movie_time.config(value=bravo_dbms_backend.get_showtimes(box_movie_name.get()))

        box_movie_name = ttk.Combobox(self.main_frame, values=movie_names)
        box_movie_name.place(x=30, y=30)
        box_movie_name.bind("<<ComboboxSelected>>",pick_times)

        #choosing a date
        def output_date():
            lbl_date = Label(self.main_frame, text=cal_movie_date.get_date(), font=("Helvetica", 13), bg="#46464a", fg="red")
            lbl_date.place(x=125, y=280)
        lbl_movie_date = custom_widgets.WhiteLabel(self.main_frame, text="Choose Date:")
        lbl_movie_date.place(x=30, y=60)
        current_date = datetime.datetime.now()
        cal_movie_date = Calendar(self.main_frame, selectmode="day", year=current_date.year, month=current_date.month, )
        cal_movie_date.place(x=30, y=85)
        enter_date_button = custom_widgets.OrangeButton(self.main_frame, text="Select Date", command=output_date)
        enter_date_button.place(x=30, y=280)

        #choosing a time
        lbl_movie_time = custom_widgets.WhiteLabel(self.main_frame, text="Choose Time:")
        lbl_movie_time.place(x=30, y=310)
        times = [" "]
        '''
        times = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00",
                 "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
                 "20:00", "21:00", "22:00", "23:00"]'''
        box_movie_time = ttk.Combobox(self.main_frame, values=times)
        box_movie_time.place(x=30, y=335)

        #added this function
        def pick_row(event):
            box_rows.config(value=bravo_dbms_backend.get_rows(box_theater.get()))

        #choosing a theater
        lbl_theater = custom_widgets.WhiteLabel(self.main_frame, text="Choose Theater:")
        lbl_theater.place(x=215, y=310)
        #rows = ["Citylight", "Starcity"]
        theaters = bravo_dbms_backend.get_theaters()
        box_theater = ttk.Combobox(self.main_frame, values=theaters)
        box_theater.place(x=215, y=335)
        box_theater.bind("<<ComboboxSelected>>",pick_row)

        def pick_seat(event):
            box_seats.config(value=bravo_dbms_backend.get_seats(box_theater.get(), box_rows.get()))

        #choosing a row
        lbl_rows = custom_widgets.WhiteLabel(self.main_frame, text="Choose Row:")
        lbl_rows.place(x=30, y=365)
        rows = [" "]
        #rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        box_rows = ttk.Combobox(self.main_frame, values=rows)
        box_rows.place(x=30, y=390)
        box_rows.bind("<<ComboboxSelected>>",pick_seat)

        #choosing a seat
        lbl_seats = custom_widgets.WhiteLabel(self.main_frame, text="Choose Seat:")
        lbl_seats.place(x=215, y=365)
        seats = [" "]
        #seats = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        box_seats = ttk.Combobox(self.main_frame, values=seats)
        box_seats.place(x=215, y=390)

        #choosing the pricing
        radio_group = StringVar()
        adult_txt="""Adult
        \u20B9 300"""
        child_txt="""Child
        \u20B9 150"""
        Student_txt="""Student
        \u20B9 200"""
        radio_adult = custom_widgets.PriceRadiobutton(self.main_frame, text=adult_txt, variable=radio_group, value="300")
        radio_child = custom_widgets.PriceRadiobutton(self.main_frame, text=child_txt, variable=radio_group, value="150")
        radio_student = custom_widgets.PriceRadiobutton(self.main_frame, text=Student_txt, variable=radio_group, value="200")
        radio_adult.place(x=30, y=430)
        radio_child.place(x=140, y=430)
        radio_student.place(x=250, y=430)

        #function for submit and clear button
        def submit_booking():
            movie = box_movie_name.get()
            date = cal_movie_date.get_date()
            time = box_movie_time.get()
            row = box_rows.get()
            seat = box_seats.get()
            price = radio_group.get()
            check_widgets = self.check_widgets(movie, date, time, row, seat, price)
            if check_widgets:
                bravo_dbms_backend.insert_booking(movie, date, time, row, seat, price, self.username)
                clear_booking()
            else:
                lbl_error = Label(self.main_frame, text=self.error_msg, fg="red", bg="#46464a", font=("Ariel", 10))
                lbl_error.place(x=160, y=489)
                lbl_error.after(8000, lbl_error.destroy)

        def clear_booking():
            box_movie_name.set(" ")
            cal_movie_date.selection_clear()
            box_movie_time.set(" ")
            box_rows.set(" ")
            box_seats.set(" ")
            radio_group.set(None)

        #buttons
        submit_button = custom_widgets.OrangeButton(self.main_frame, text="Submit", command=submit_booking)
        submit_button.place(x=30, y=489)
        clear_button = Button(self.main_frame, text="Clear", bg="grey", fg="white", padx=5, command=clear_booking)
        clear_button.place(x=105, y=489)


    #to reset the buttons background
    def button_background(self):
        self.movies.config(bg="#46464a", relief="raised")
        self.add_movie.config(bg="#46464a", relief="raised")
        self.bookings.config(bg="#46464a", relief="raised")
        self.add_booking.config(bg="#46464a", relief="raised")

    #view movies
    def view_movies_UI(self):
        User.view_movies_UI(self)

        #funtion for remove button
        def remove_movie():
            movie_id = txt_move_id.get()
            bravo_dbms_backend.remove_movie(movie_id)
            txt_move_id.delete(0, END)

        lbl_movie_id = custom_widgets.WhiteLabel(self.main_frame,  text="Enter Movie ID: ")
        lbl_movie_id.place(x=230, y=270)
        txt_move_id = custom_widgets.GreyEntry(self.main_frame)
        txt_move_id.place(x=230, y=293)
        
        #remove movie button
        remove_movie_button = custom_widgets.OrangeButton(self.main_frame, text="Remove Movie", command=remove_movie)
        remove_movie_button.place(x=460, y=290)

    #add movie
    def add_movie_UI(self):
        self.button_background()
        self.add_movie.config(bg="#2c2c2e", relief = "sunken")
        self.delete_widgets()

        #entry boxes
        lbl_movie_name = custom_widgets.WhiteLabel(self.main_frame, text="Movie Name:")
        lbl_movie_name.place(x=30, y=5)
        txt_movie_name = custom_widgets.GreyEntry(self.main_frame)
        txt_movie_name.place(x=30, y=30)

        lbl_run_time = custom_widgets.WhiteLabel(self.main_frame, text="Movie Length (minutes):")
        lbl_run_time.place(x=30, y=70)
        txt_run_time = custom_widgets.GreyEntry(self.main_frame)
        txt_run_time.place(x=30, y=95)

        lbl_genre = custom_widgets.WhiteLabel(self.main_frame, text="Movie Genre/Genres:")
        lbl_genre.place(x=30, y=135)
        txt_genre = custom_widgets.GreyEntry(self.main_frame)
        txt_genre.place(x=30, y=160)

        #function for submit and clear button
        def submit_movie():
            name = txt_movie_name.get()
            run_time = txt_run_time.get()
            genre = txt_genre.get()
            check_widgets = self.check_widgets(name, run_time, genre)
            if check_widgets:
                bravo_dbms_backend.insert_movie(name, run_time, genre)
                clear_movie()
            else:
                lbl_error = Label(self.main_frame, text=self.error_msg, fg="red", bg="#46464a", font=("Ariel", 10))
                lbl_error.place(x=160, y=193)
                lbl_error.after(8000, lbl_error.destroy)

        def clear_movie():
            txt_movie_name.delete(0, END)
            txt_run_time.delete(0, END)
            txt_genre.delete(0, END)
            
        #buttons
        submit_button = custom_widgets.OrangeButton(self.main_frame, text="Submit", command=submit_movie)
        submit_button.place(x=30, y=193)
        clear_button = Button(self.main_frame, text="Clear", bg="grey", fg="white", padx=5, command=clear_movie)
        clear_button.place(x=100, y=193)

    #view bookings
    def view_bookings_UI(self):
        self.button_background()
        self.bookings.config(bg="#2c2c2e", relief = "sunken")
        self.delete_widgets()

        #main label
        lbl_all_bookings = Label(self.main_frame, text="All Bookings", font=("Helvetica", 13), bg="#46464a", fg="red")
        lbl_all_bookings.place(x=50, y=0)
        bookings_frame = Frame(self.main_frame, bg="white")
        bookings_frame.place(x=50, y=30)

        tree_scroll = Scrollbar(bookings_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        #tree view table
        #booking_tree = ttk.Treeview(bookings_frame, column=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), show='headings', yscrollcommand=tree_scroll.set)
        movie_tree = ttk.Treeview(bookings_frame, column=("#1", "#2", "#3", "#4", "#5","#6","#7","#8","#9","#10"), show='headings')
        #table customisation
        tree_style = ttk.Style()
        tree_style.theme_use("clam")
        tree_style.configure("Treeview", background="#46464a",
                        fieldbackground="#46464a", foreground="white")
        tree_style.map('Treeview', background=[("selected", "#2c2c2e")])

        tree_scroll.config(command=movie_tree.yview)
        #columns and headings
        movie_tree.column("#1", anchor=CENTER, width=60)
        movie_tree.column("#2", anchor=CENTER, width=60)
        movie_tree.column("#3", anchor=CENTER, width=60)
        movie_tree.column("#4", anchor=CENTER, width=60)
        movie_tree.column("#5", anchor=CENTER, width=60)
        movie_tree.column("#6", anchor=CENTER, width=60)
        movie_tree.column("#7", anchor=CENTER, width=60)
        movie_tree.column("#8", anchor=CENTER, width=60)
        movie_tree.column("#9", anchor=CENTER, width=60)
        movie_tree.column("#10", anchor=CENTER, width=60)
        movie_tree.heading("#1", text="Booking_ID")
        movie_tree.heading("#2", text="Username")
        movie_tree.heading("#3", text="movie_id")
        movie_tree.heading("#4", text="movie_name")
        movie_tree.heading("#5", text="Date")
        movie_tree.heading("#6", text="time")
        movie_tree.heading("#7", text="row")
        movie_tree.heading("#8", text="seat")
        movie_tree.heading("#9", text="Price")    
        movie_tree.heading("#10", text="Theater")     
        movie_tree.pack()

        #function for display and remove buttons
        def view_bookings():
            for row in movie_tree.get_children():
                movie_tree.delete(row)
            order = box_order_booking.get()
            rows = bravo_dbms_backend.get_all_bookings(order)
            for row in rows:
                movie_tree.insert("", END, values=row)

        def remove_booking():
            booking_id = txt_booking_id.get()
            bravo_dbms_backend.remove_booking(booking_id)
            txt_booking_id.delete(0, END)

        #order bookings option
        lbl_order_booking = custom_widgets.WhiteLabel(self.main_frame, text="Order by:")
        lbl_order_booking.place(x=390, y=0)
        booking_columns = ["booking_id", "movie_id", "date", "time", "row", "seat", "price"]
        box_order_booking = ttk.Combobox(self.main_frame, values=booking_columns)
        box_order_booking.place(x=460, y=0)

        #display button
        display_bookings = custom_widgets.OrangeButton(self.main_frame, text="Display Bookings", command=view_bookings)
        display_bookings.place(x=50, y=290)

        lbl_booking_id = custom_widgets.WhiteLabel(self.main_frame,  text="Enter Booking ID: ")
        lbl_booking_id.place(x=230, y=270)
        txt_booking_id = custom_widgets.GreyEntry(self.main_frame)
        txt_booking_id.place(x=230, y=293)

        #remove button
        remove_booking_button = custom_widgets.OrangeButton(self.main_frame, text="Remove Booking", command=remove_booking)
        remove_booking_button.place(x=460, y=290)
#================================================================================================================================================================

def start_admin(username):
    root = Tk()
    root.geometry("1000x1000")
    root.title("CINE APP")
    root.configure(background="#46464a")
    logo = PhotoImage(file="logo.png")
    root.iconphoto(True, logo)
    bravo = Admin(root, logo,username)
    root.mainloop()

def start_user(username):
    root = Tk()
    root.geometry("1000x1000")
    root.title("CINE APP")
    root.configure(background="#46464a")
    logo = PhotoImage(file="logo.png")
    root.iconphoto(True, logo)
    bravo = User(root, logo,username)
    root.mainloop()

if __name__ == "__main__":
    start_admin()
