import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="UniversityManagement"
)

if db.is_connected():
    print("Connected to MySQL Database")

cursor = db.cursor(buffered=True)

# CREATE Operations
def create_course(course_id, course_name, department):
    try:
        query = "INSERT INTO Courses (CourseID, CourseName, Department) VALUES (%s, %s, %s)"
        cursor.execute(query, (course_id, course_name, department))
        db.commit()
        print(f"Course '{course_name}' has been added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_student(student_id, name, email, course_id):
    try:
        query = "INSERT INTO Students (StudentID, Name, Email, CourseID) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (student_id, name, email, course_id))
        db.commit()
        print(f"Student '{name}' has been added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_faculty(faculty_id, name, email, department):
    try:
        query = "INSERT INTO Faculty (FacultyID, Name, Email, Department) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (faculty_id, name, email, department))
        db.commit()
        print(f"Faculty '{name}' has been added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_enrollment(enrollment_id, student_id, course_id):
    try:
        query = "INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID) VALUES (%s, %s, %s)"
        cursor.execute(query, (enrollment_id, student_id, course_id))
        db.commit()
        print(f"Enrollment '{enrollment_id}' has been added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# READ Operations
def read_students():
    try:
        cursor.execute("SELECT * FROM Students")
        result = cursor.fetchall()
        print("Students:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def read_courses():
    try:
        cursor.execute("SELECT * FROM Courses")
        result = cursor.fetchall()
        print("Courses:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def read_enrollments():
    try:
        cursor.execute("""
            SELECT Enrollments.EnrollmentID, Students.Name, Courses.CourseName 
            FROM Enrollments
            JOIN Students ON Enrollments.StudentID = Students.StudentID
            JOIN Courses ON Enrollments.CourseID = Courses.CourseID
        """)
        result = cursor.fetchall()
        print("Enrollments:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# UPDATE Operations
def update_student_email(student_id, new_email):
    try:
        query = "UPDATE Students SET Email = %s WHERE StudentID = %s"
        cursor.execute(query, (new_email, student_id))
        db.commit()
        print(f"Student '{student_id}' email has been updated to '{new_email}'.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_course_name(course_id, new_name):
    try:
        query = "UPDATE Courses SET CourseName = %s WHERE CourseID = %s"
        cursor.execute(query, (new_name, course_id))
        db.commit()
        print(f"Course '{course_id}' name has been updated to '{new_name}'.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# DELETE Operations
def delete_student(student_id):
    try:
        query = "DELETE FROM Students WHERE StudentID = %s"
        cursor.execute(query, (student_id,))
        db.commit()
        print(f"Student '{student_id}' has been deleted.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_course(course_id):
    try:
        query = "DELETE FROM Courses WHERE CourseID = %s"
        cursor.execute(query, (course_id,))
        db.commit()
        print(f"Course '{course_id}' has been deleted.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_enrollment(enrollment_id):
    try:
        query = "DELETE FROM Enrollments WHERE EnrollmentID = %s"
        cursor.execute(query, (enrollment_id,))
        db.commit()
        print(f"Enrollment '{enrollment_id}' has been deleted.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Main Menu
def main_menu():
    while True:
        print("\nUniversity Management System")
        print("1. Add a Course")
        print("2. Add a Student")
        print("3. Add a Faculty")
        print("4. Enroll a Student")
        print("5. View Students")
        print("6. View Courses")
        print("7. View Enrollments")
        print("8. Update Student Email")
        print("9. Update Course Name")
        print("10. Delete a Student")
        print("11. Delete a Course")
        print("12. Delete an Enrollment")
        print("13. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            course_id = input("Course ID: ")
            course_name = input("Course Name: ")
            department = input("Department: ")
            create_course(course_id, course_name, department)
        elif choice == "2":
            student_id = input("Student ID: ")
            name = input("Name: ")
            email = input("Email: ")
            course_id = input("Course ID: ")
            create_student(student_id, name, email, course_id)
        elif choice == "3":
            faculty_id = input("Faculty ID: ")
            name = input("Name: ")
            email = input("Email: ")
            department = input("Department: ")
            create_faculty(faculty_id, name, email, department)
        elif choice == "4":
            enrollment_id = input("Enrollment ID: ")
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            create_enrollment(enrollment_id, student_id, course_id)
        elif choice == "5":
            read_students()
        elif choice == "6":
            read_courses()
        elif choice == "7":
            read_enrollments()
        elif choice == "8":
            student_id = input("Student ID: ")
            new_email = input("New Email: ")
            update_student_email(student_id, new_email)
        elif choice == "9":
            course_id = input("Course ID: ")
            new_name = input("New Course Name: ")
            update_course_name(course_id, new_name)
        elif choice == "10":
            student_id = input("Student ID: ")
            delete_student(student_id)
        elif choice == "11":
            course_id = input("Course ID: ")
            delete_course(course_id)
        elif choice == "12":
            enrollment_id = input("Enrollment ID: ")
            delete_enrollment(enrollment_id)
        elif choice == "13":
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

main_menu()  