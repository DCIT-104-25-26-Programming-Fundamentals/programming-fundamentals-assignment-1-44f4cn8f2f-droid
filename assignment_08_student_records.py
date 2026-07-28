# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
=============================================================================
def add_student(students):
	name = input("Student name: ").strip()
	if not name:
		print("Name cannot be empty.")
		return

	while True:
		sid = input("Student ID: ").strip()
		if not sid:
			print("ID cannot be empty.")
			continue
		# keep ID as string to preserve leading zeros if any
		if any(s['id'] == sid for s in students):
			print("A student with that ID already exists.")
			return
		break

	while True:
		try:
			n = int(input("How many scores? "))
			if n < 0:
				print("Please enter a non-negative number.")
				continue
			break
		except ValueError:
			print("Please enter an integer number.")

	scores = []
	for i in range(1, n + 1):
		while True:
			try:
				s = float(input(f"Enter score {i}: "))
				scores.append(int(s) if s.is_integer() else s)
				break
			except ValueError:
				print("Please enter a numeric score.")

	student = {"name": name, "id": sid, "scores": scores}
	students.append(student)
	print(f'Student "{name}" added successfully.')


def display_all_students(students):
	if not students:
		print("No students have been added yet.")
		return

	print("--------------------------------------------------")
	print(f"{'Name':<15} {'ID':<10} {'Scores':<15} Average")
	print("--------------------------------------------------")
	for s in students:
		scores_str = ", ".join(str(x) for x in s['scores']) if s['scores'] else ""
		avg = round(sum(s['scores']) / len(s['scores']), 2) if s['scores'] else 0.00
		print(f"{s['name']:<15} {s['id']:<10} {scores_str:<15} {avg:.2f}")
	print("--------------------------------------------------")


def calculate_average_for_student(students):
	sid = input("Enter student ID: ").strip()
	for s in students:
		if s['id'] == sid:
			if not s['scores']:
				print(f"{s['name']} has no scores.")
				return
			avg = round(sum(s['scores']) / len(s['scores']), 2)
			print(f"{s['name']}'s average score: {avg:.2f}")
			return
	print("Student ID not found.")


def main():
	students = []
	while True:
		print("===============================")
		print("   STUDENT RECORD SYSTEM MENU")
		print("===============================")
		print("1. Add student")
		print("2. Display all students")
		print("3. Calculate average score")
		print("4. Quit")
		choice = input("Enter your choice (1-4): ").strip()

		if choice == '1':
			add_student(students)
		elif choice == '2':
			display_all_students(students)
		elif choice == '3':
			calculate_average_for_student(students)
		elif choice == '4':
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == '__main__':
	main()


