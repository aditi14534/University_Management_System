University_Management_System
A Python-MySQL based University Management System to handle student, course, and faculty records efficiently.

Features
🎓 Student Management (Add, Update, Delete, View)

📚 Course Management

🏫 Faculty Management

🔑 Secure Authentication 

Tech Stack
Programming Language: Python
Database: MySQL
Libraries Used: mysql-connector-python

How to Run the Project
1. Install Python
Ensure Python 3.x is installed.

Check by running: python --version
2. Install Required Dependencies
Run the following command to install necessary libraries:
pip install mysql-connector-python

3. Set Up MySQL Database
Open MySQL and create the database:
CREATE DATABASE UniversityManagement;

Import the provided SQL script (if available) to set up tables.

Update database credentials in college.py or the relevant Python script:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database=" UniversityManagement"
)

4. Run the Project
   python college.py
