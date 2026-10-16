class NameException(Exception):
    pass

class HomeRoomException(Exception):
    pass

class DuplicateStudentException(Exception):
    pass



# Method that adds students based on the amount of students that the user wants to add

def addStudent(student_list, amount_ofstudents):
    #It will capture information of students which will be:
    # Name, homeroom, spanish grade, english grade, science grade, and social studies grade
    try:
        for _ in range(amount_ofstudents):
            student = {}
            student["name"] = input("Enter the student's name: ")

            if is_empty_name(student["name"]) or has_numbers(student["name"]):
                raise NameException

            student["homeroom"] = input("Enter the student's homeroom: ")
            if not is_valid_homeroom(student["homeroom"]):
                raise HomeRoomException

            # Exception that captures duplicate students
            if has_duplicate_students(student_list, student["name"], student["homeroom"]):
                raise DuplicateStudentException
            
            student["spanish_grade"] = float(input("Enter the student's Spanish grade: "))
            if not is_valid_grade(student["spanish_grade"]):
                raise ValueError


            student["english_grade"] = float(input("Enter the student's English grade: "))
            if not is_valid_grade(student["english_grade"]):
                raise ValueError

            student["science_grade"] = float(input("Enter the student's Science grade: "))
            if not is_valid_grade(student["science_grade"]):
                raise ValueError

            student["social_studies_grade"] = float(input("Enter the student's Social Studies grade: "))
            if not is_valid_grade(student["social_studies_grade"]):
                raise ValueError

            student_list.append(student)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except NameException:
        print("Invalid name. It cannot be empty or have numbers.")

    except HomeRoomException:
        print("Invalid homeroom. It must be a letter followed by a number.")
    except DuplicateStudentException:
        print("Duplicate student found. Please enter a unique name and homeroom.")


# Method that recieves a grade and returns if it is a grade higher than 0 and lower than 101.
def is_valid_grade(grade):
    if grade >= 0 and grade <= 100:
        return True
    else:
        return False
    

# Method that checks if the student name is empty and if it is not, it returns false, if it is empty it returns true.
def is_empty_name(name):
    if name == "":
        return True
    else:
        return False

# Method that identifies and returns if a student name is in fact with numbers or not
def has_numbers(name):
    # char digit loop every character in the name and returns true if it finds a number.
    if any(char.isdigit() for char in name):
        return True
    else:
        return False

# Method that identifies a homeroom and determines if it has the correct format, 
# which is a letter followed by a number, for example A1, B2, C3, etc. 
def is_valid_homeroom(homeroom):
    # Check if the homeroom is a string and has a length of 2, 
    # and if the first character is a letter and the second character is a digit.
    if len(homeroom) == 2 and homeroom[0].isalpha() and homeroom[1].isdigit():
        return True
    else:
        return False 

# Method that identifies if there are students with the same name and homeroom, 
# if there are, it returns true, if not, it returns false.
def has_duplicate_students(student_list, name, homeroom):
    for student in student_list:
        if student["name"] == name and student["homeroom"] == homeroom:
            return True
    return False

def showStudents(student_list):
    if not student_list:
        print("No students have been added yet.")
        return

    for student in student_list:
        print(f"Name: {student['name']}, Homeroom: {student['homeroom']}, "
            f"Spanish Grade: {student['spanish_grade']}, English Grade: {student['english_grade']}, "
            f"Science Grade: {student['science_grade']}, Social Studies Grade: {student['social_studies_grade']}")


def top_3_major_grade_point_average(student_list):
    if not student_list:
        print("No students have been added yet.")
        return

    first_grade = 0
    second_grade = 0
    third_grade = 0

    # Calculate the average grade for each student
    for student in student_list:
        grades = [student["spanish_grade"], student["english_grade"], student["science_grade"], student["social_studies_grade"]]
        student["average_grade"] = sum(grades) / len(grades)
        if student["average_grade"] > first_grade:
            first_grade = student["average_grade"]
        if student["average_grade"] > second_grade and student["average_grade"] < first_grade:
            second_grade = student["average_grade"]
        if student["average_grade"] > third_grade and student["average_grade"] < second_grade:
            third_grade = student["average_grade"]

    # Sort the students by average grade in descending order
    #sorted_students = sorted(student_list, key=lambda x: x["average_grade"], reverse=True)

    # Get the top 3 students
    #top_3_students = sorted_students[:3]

    print("Top 3 Students by Average Grade:")
    for student in student_list:
        if student["average_grade"] == first_grade:
            print(f"1. Name: {student['name']}, Average Grade: {student['average_grade']:.2f}")
        elif student["average_grade"] == second_grade:
            print(f"2. Name: {student['name']}, Average Grade: {student['average_grade']:.2f}")
        elif student["average_grade"] == third_grade:
            print(f"3. Name: {student['name']}, Average Grade: {student['average_grade']:.2f}")

# Method that calculates the average of all averages of the students and returns it.
def calculate_overall_average(student_list):
    if not student_list:
        return 0
    # Atribute that will store the total average of all students
    total_average = 0

    # Loop through the student list and calculate the average of each student and add it to the total average
    for student in student_list:
        grades = [student["spanish_grade"], student["english_grade"], student["science_grade"], student["social_studies_grade"]]
        total_average += sum(grades) / len(grades)
    overall_average = total_average / len(student_list)
    return overall_average

# Method that exports all the previous methods into a CSV.
def export_to_csv(student_list, filename):
    import csv
    if not student_list:
        print("No students have been added yet.")
        return

    with open(filename, mode='w', newline='') as file:
        writer = csv

def eliminate_student_by_name_and_homeroom(student_list):
    # data is obtaines
    name = input("Enter the student's name: ")
    homeroom = input("Enter the student's homeroom: ")

    # Loop through the student list and remove the student with the matching name and homeroom
    for student in student_list:
        if student["name"] == name and student["homeroom"] == homeroom:
            student_list.remove(student)
            print(f"Student {name} from homeroom {homeroom} has been removed.")
            return
    print(f"No student found with name {name} and homeroom {homeroom}.")


# Method that shows failed students that have an average lower than 70.
def show_failed_students(student_list):

    # store the failed students in a list
    failed_students = []

    # Loop through the student list and check if the average grade is lower than 70
    for student in student_list:
        grades = [student["spanish_grade"], student["english_grade"], student["science_grade"], student["social_studies_grade"]]       
        # Loop throught the student grades and if tehres at least 1 grade lower than 60
        # the student is considered failed and is added to the failed_students list
        for grade in grades:
            if grade < 60:
                failed_students.append(student)
                break

    # It shows the information
    if failed_students:
        print("Failed Students (Average Grade < 60):")
        for student in failed_students:
            print(f"Name: {student['name']}, Homeroom: {student['homeroom']}, Spanish Grade: {student['spanish_grade']}, English Grade: {student['english_grade']}, science Grade: {student['science_grade']}, Social Studies Grade: {student['social_studies_grade']}")
    else:
        print("No students have failed.")

