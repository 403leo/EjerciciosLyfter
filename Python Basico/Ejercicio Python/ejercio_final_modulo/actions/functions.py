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

            while True:
                student = {}


                # Request a valid name.
                student["name"] = get_valid_name("name")
                student["homeroom"] = get_valid_homeroom("homeroom")

                # Exception that captures duplicate students
                if has_duplicate_students(student_list, student["name"], student["homeroom"]):
                    print("Duplicate student found. Please enter a unique name and homeroom.")
                    continue

                
                
                # Request each grade until it is valid.
                student["spanish_grade"] = get_valid_grade("Spanish")
                student["english_grade"] = get_valid_grade("English")
                student["science_grade"] = get_valid_grade("Science")
                student["social_studies_grade"] = get_valid_grade("Social Studies")


                # Add the student only after all fields are valid.
                student_list.append(student)

                break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Method that requests a valid grade for a subject, 
# if the user enters an invalid grade, 
# it will ask again until a valid grade is entered.
def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the student's {subject} grade: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not is_valid_grade(grade):
            print("Invalid grade. The grade must be between 0 and 100.")
            continue
        return grade
    




# Method that recieves a grade and returns if it is a grade higher than 0 and
#  lower than 101.
# It will also not end the loop until the user enters a valid grade, and it will return the valid grade.
def is_valid_grade(grade):
    while True:
        if grade >= 0 and grade <= 100:
            return True
            continue
        else:
            return False
            continue
    

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

def get_valid_name(subject):
    while True:
        try:
            name = input(f"Enter the student's {subject} name: ")

        except ValueError:
            print("Invalid input. Please enter a valid name.")
            continue

        if is_empty_name(name) or has_numbers(name):
            print("Invalid name. It cannot be empty or have numbers.")
            continue
        
        return name

# Method that identifies a homeroom and determines if it has the correct format, 
# which is a letter followed by a number, for example A1, B2, C3, etc. 
def is_valid_homeroom(homeroom):
    # Check if the homeroom is a string and has a length of 2 or more
    # and if the first character is a number and the second character is a letter.
    if len(homeroom) >= 2 and homeroom[:-1].isdigit() and homeroom[-1].isalpha():
        return True
    else:
        return False 

def get_valid_homeroom(subject):
    while True:
        try:
            homeroom = input(f"Enter the student's {subject} subject: ")

        except ValueError:
            print("Invalid input. Please enter a valid homeroom.")
            continue

        if not is_valid_homeroom(homeroom):
            print("Invalid homeroom. It must be a letter followed by a number.")
            continue
        
        return homeroom

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

    # Calculate the average grade for each student
    for student in student_list:
        grades = [student["spanish_grade"], student["english_grade"], student["science_grade"], student["social_studies_grade"]]
        student["average_grade"] = sum(grades) / len(grades)

    # Sort the students by average grade in descending order
    sorted_students = sorted(
        student_list, 
        key=lambda x: x["average_grade"], 
        reverse=True)

    # Get the top 3 students
    top_3_students = sorted_students[:3]

    print("Top 3 Students by Average Grade:")
    for position, student in enumerate(top_3_students, start=1):
        print(f"{position}. Name: {student['name']}, Homeroom: {student['homeroom']}, Average Grade: {student['average_grade']:.2f}")

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
    # data is obtained
    name = input("Enter the student's name: ")
    homeroom = input("Enter the student's homeroom: ")

    # Loop through the student list and remove the student with the matching name and homeroom
    for student in student_list:
        if student["name"] == name and student["homeroom"] == homeroom:

            # The system asks first if the user is sure about eliminating the student, if the user says yes, it will eliminate the student, if the user says no, it will return to the main menu.
                confirmation = input(f"Are you sure you want to remove the student {name} from homeroom {homeroom}? (yes/no): ")
                if confirmation.lower() != "yes":
                    print("Operation cancelled.")
                    return

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
        grades = {
            "spanish": student["spanish_grade"],
            "english": student["english_grade"],
            "science": student["science_grade"],
            "social_studies": student["social_studies_grade"]
        }
        
        # Store the failed subjects of the students in a list
        failed_subjects = {}
        
        # Loop throught the student grades and if tehres at least 1 grade lower than 60
        # the student is considered failed and is added to the failed_subjects list
        for subject, grade in grades.items():
            if grade < 60:
                failed_subjects[subject] = grade

        # add the student only if at least one subject was failed
        if failed_subjects:
            failed_students.append({
                "name": student["name"],
                "homeroom": student["homeroom"],
                "failed_subjects": failed_subjects
            })

    # It shows exclusively only the grades of the subjects of the students that have failed, and it shows the name, homeroom, and grades of those failed subjects.
    if failed_students:
        print("Students with Failed Subjects:")
        for student in failed_students:
            print(f"Name: {student['name']}, Homeroom: {student['homeroom']}")

            for subject, grade in student["failed_subjects"].items():
                print(f"  Subject:{subject} Grade: {grade}")
    else:
        
        print("No students have failed.")

