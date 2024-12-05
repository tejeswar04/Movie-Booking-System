# 🎬 Movie Booking Database System  

A comprehensive database-driven system for managing movie bookings. This project enables users to view movie details, book tickets, and manage their reservations. Admins can manage movies, showtimes, and bookings seamlessly.  

## 📚 Table of Contents  
- [Project Overview](#project-overview)  
- [Features](#features)  
- [ER Diagram and Relational Tables](#er-diagram-and-relational-tables)  
- [UI Design](#ui-design)  
- [Technologies Used](#technologies-used)  
- [Setup Instructions](#setup-instructions)

---

## 📝 Project Overview  

This project is developed as part of the **Database Systems Lab (CSE 2262)** course at **Manipal Institute of Technology**. It utilizes a relational database in BCNF form and integrates SQL queries with a Python-based UI.  

### Key Features  
- **User Functionality**:  
  - 🎥 View movie details (name, runtime, genre)  
  - 🍿 Book tickets based on available showtimes and seats  
  - 🎟️ View personal booking history  
- **Admin Functionality**:  
  - ✏️ Add, update, and delete movies and showtimes  
  - 🛠️ Manage and view user bookings  
  - 🔄 Execute SQL queries manually  

---

## 📊 ER Diagram and Relational Tables  

The database is designed in **BCNF** form, with the following relational tables:  
- **Movies**: Stores movie details (ID, name, runtime, genre)  
- **Bookings**: Stores booking information (ID, user, movie, date, time, seat, price)  
- **Showtimes**: Stores available showtimes for movies  
- **Theatres**: Stores available theatres  
- **Seats**: Stores seat information in each theatre  
- **Users**: Stores user details (ID, username, password, contact)  
- **Admin**: Stores admin credentials  

### ER Diagram  
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/ER.jpeg)

---

## 🎨 UI Design  

The project features a user-friendly interface with the following key screens:  
- **Login**
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/LogIN.png)
- **Sign-Up**
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/signup.png)
- **View Movies**
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/view_movies.png)
- **View Bookings**
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/view_b.png)
- **Add Booking**
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/add_b.png)
- **Admin-Dashboard**
![alt text](https://github.com/tejeswar04/Movie-Booking-System/blob/main/imgs/admin.png)

---

## 💻 Technologies Used  

- **Python**: For backend logic and database interaction  
- **SQLite3**: For database management  
- **Tkinter**: For creating the graphical user interface (GUI)  
- **SQL**: For handling queries and database operations  
- **Simple Crypt**: For secure password encryption  

---

## 🚀 Setup Instructions  

To run this project locally, follow these steps:

1. **Clone the Repository**  
   First, clone the project repository to your local machine:  
   ```bash
   git clone https://github.com/your-username/movie-booking-system.git
   ```
2.**Pip install Dependencies**
  Now install the dependecies using the below command
  ```bash
  pip install -r requirements.txt
  ```
3.**Run the python file**
  Now we need to run the python file
  ``` bash
  python loginSystem.py
  ```
---

## 📑 References  

Here are some useful resources used during the development of this project:

- [SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)  
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [Simple Crypt Library](https://pypi.org/project/simple-crypt/)  
- [Entity Relationship Diagram Tool](https://www.smartdraw.com/entity-relationship-diagram/er-diagram-tool.htm)  
- [Python Programming YouTube Tutorials](https://www.youtube.com/watch?v=YXPyB4XeYLA)  
- [Python SQLite3 Tutorial](https://www.youtube.com/watch?v=byHcYRpMgI4)  
- [Tkinter GUI Tutorials](https://www.youtube.com/watch?v=TY6RDEG9bhw)  


