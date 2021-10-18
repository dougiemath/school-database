import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('SchoolDatabase')

student_data = SHEET.worksheet('studentdata')
data = student_data.get_all_values()

def start():
    """
    Adds a contents menu for users to navigate
    """
    print("""
                --------MENU--------
                1. Add new student
                2. Search student
                3. Check Level
                4. Show all students
                5. Exit
                    """)
    while True:
        selection = input("Pick a number: \n")
        if selection == '1':
            add_student()
            break
        elif selection == '2':
            search_student()
            break
        elif selection == '3':
            display_all_students()
            break
        elif selection == '4':
            check_level()
            break
        elif selection == '5':
            exit()
            break
        else:
            print("Invalid choice, please enter a number 1-3")

def add_student():
    print("""You will be asked to input the following data:
    Family Name, First Name(s), Email Address, Age, Nationality, Course Start/End Date, and Test Results\n""")
    family_name = input("Please Enter the student's family name: ")
    first_name = input("Please Enter the student's first name(s): ")
    email_address = input("Please Enter the student's email: ")
    student_age = input("Please Enter the student's age: ")
    student_nationality = input("Please Enter the student's nationality: ")
    student_course_start = input("Please Enter the student's course start date: ")
    student_course_end = input("Please Enter the student's course end date: ")
    student_test_results = input("Please Enter the student's course test results: ")
    print("You have entered the following details:")
    print(f"Family name: {family_name}.")
    print(f"First name(s): {first_name}.")
    print(f"Email address: {email_address}.")
    print(f"Age: {student_age}.")
    print(f"Nationality: {student_nationality}.")
    print(f"Starting date of course: {student_course_start}.")
    print(f"End date of course: {student_course_end}.")
    print(f"Test results {student_test_results}.")
        
    confirmation = input("Is the data correct? Y/N")

def search_student():
    print("this is the search student")

def display_all_students():
    print("This displays everyone")

def check_level():
    print("This checks level")

def exit():
    print("this is the end")

def main():
    start()

add_student()
