# Create a dictionary of student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68,
    "Ethan": 78
}

# Ask user for a student name
student_name = input("Enter student's name: ")

# Retrieve and display marks or show message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
