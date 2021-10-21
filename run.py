import datetime
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
STUDENTS = SHEET.worksheet("studentdata")


def add_new_student():
    """
    Function to add new student by name, age
    test results, and course dates
    """
    student_details = []
    while True:
        family_name = input("Please enter the student's family name: ")
        validate_data(family_name)
       
        if validate_data(family_name):
            student_details.append(family_name)
            break

    while True:
        first_name = input("Please enter the student's first name: ")
        validate_data(first_name)
       
        if validate_data(first_name):
            student_details.append(first_name)
            break
    
    while True:
        nationality = input("Please enter the student's nationality: ")
        validate_data(nationality)
       
        if validate_data(nationality):
            student_details.append(nationality)
            break

    while True:
        age = input("Please enter the student's age: ")
        validate_numeric_data(age)
       
        if validate_numeric_data(age):
            student_details.append(int(age))
            break

    while True:
        test_results = input("Please enter the student's test results: ")
        validate_numeric_data(test_results)

        if int(test_results) >=30:
            print("please enter a score from 1-30")
            continue
        
        if validate_numeric_data(test_results):
            student_details.append(int(test_results))
            break

    while True:
        if int(test_results) >= 1 and int(test_results) <= 5:
            student_level = "A1"
        elif int(test_results) >= 6 and int(test_results) <= 10:
            student_level = "A2"
        elif int(test_results) >= 11 and int(test_results) <= 15:
            student_level = "B1"
        elif int(test_results) >= 16 and int(test_results) <= 23:
            student_level = "B2"
        elif int(test_results) >= 23 and int(test_results) <= 28:
            student_level = "C1"
        elif int(test_results) >= 29 and int(test_results) <= 30:
            student_level = "C2"

        student_details.append(student_level)
        break
    
    while True:
        try:
            start_date = input("Please enter the start date: ")
            validate_date(start_date)
            end_date = input("Please enter the end date: ")
            validate_date(end_date) 
        
            if validate_date(start_date) and validate_date(end_date) and end_date > start_date:
                student_details.append(start_date)
                student_details.append(end_date)
                break
            else:
               print("Nope")
               
        except Exception:
            pass

    #generates student number
    max_rows = len(STUDENTS.get_all_values()) 
    print(max_rows)
    student_number = int(max_rows) + 1
    student_details.append(student_number)

    headings = STUDENTS.row_values(1) 
    summary = dict(zip(headings, student_details))
    print("-----------")
    for x, y in summary.items():
        print(f"{x}: {y}")
    print("-----------")

    while True:
        
        confirmation = input("Do you wish to add this student to the database? (Y/N) ")
    
        if confirmation == "Y" or confirmation == "y":
            print("Good")
        elif confirmation == "N" or confirmation == "n":
            print("oh....")
            next_step = input("Do you want to add a new student? (Y/N) ")
            if next_step == "Y" or next_step == "y":
                print("Good1")
                add_new_student()
            elif next_step == "N" or next_step == "n":
                exit()
        else:
            print("Please enter 'Y' or 'N'")



    #add data to google sheet
    #SHEET.worksheet('studentdata').append_row(student_details)



"""
Functions for validating user input in
add_new_student()
"""
def validate_data(values):
    try:
        if values.isalpha() == False:
            raise ValueError(
                    "please make sure you only use letters.  Special characters are not allowed "
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
   
    return True

def validate_numeric_data(values):
    try:
        if values.isnumeric() == False:
            raise ValueError(
                    "please make sure you only use numbers."
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def validate_date(values):
    try:
        if datetime.datetime.strptime(values, '%d-%m-%Y') == False:
            raise ValueError(
                    "please make sure you only use numbers."
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

"""
function to display values as a list
"""
def display_all_students():
    wks = STUDENTS.get_all_records()
    if wks:
        for student in wks:
            print_all_students(student)
    else:
        print("None")

def print_all_students(existing):
    student = []
    print("---")
    for key, value in existing.items():
        print(f'{key}: {value}')
    print("---")
    return student
"""
function to search by surname
"""
def search_for_student():
    username = input('Family name: ')
    test = STUDENTS.col_values(2)
    if username in test:
        rownum = test.index(username) + 1
        row = STUDENTS.row_values(rownum)
        headings = STUDENTS.row_values(1) 
        search_results = dict(zip(headings, row))
        print("------")
        for x, y in search_results.items():
            print(x, ": ", y)
        print("------")

def exit():
    print("bye bye")
    quit()
    

add_new_student()
#display_all_students()
#search_for_student()


