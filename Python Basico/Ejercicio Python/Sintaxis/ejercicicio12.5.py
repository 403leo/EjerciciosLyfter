student_number_of_subjects = int(input("Enter the number of subjects you currently have: "))
approved_subjects = 0
failed_subjects = 0
average_subjects = 0 
average_approved_subjects = 0 
average_failed_subjects = 0 
current_subject = 0
student_subject_counter = 1


while student_subject_counter <= student_number_of_subjects:
	current_subject = int(input(f"Enter the score number {student_subject_counter}: "))
	if current_subject >= 70:
		approved_subjects = approved_subjects + 1
		average_approved_subjects = average_approved_subjects + current_subject
	if current_subject < 70:
		failed_subjects = failed_subjects + 1
		average_failed_subjects = average_failed_subjects + current_subject
	average_subjects = average_subjects + current_subject
	student_subject_counter = student_subject_counter + 1

if approved_subjects != 0:
	average_approved_subjects = average_approved_subjects / approved_subjects
if failed_subjects != 0:
	average_failed_subjects = average_failed_subjects / failed_subjects
average_subjects = average_subjects / student_number_of_subjects

print(f"The number of approved subjects is: {approved_subjects}")
print(f"The number of failed subjects is: {failed_subjects}")
print(f"The average of all subjects is: {average_subjects}")
print(f"The average of approved subjects is: {average_approved_subjects}")
print(f"The average of failed subjects is: {average_failed_subjects}")