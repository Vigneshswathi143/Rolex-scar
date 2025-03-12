students = [
    {"name": "John", "subject": "Math", "marks": 85},
    {"name": "Alice", "subject": "Science", "marks": 78},
    {"name": "Bob", "subject": "English", "marks": 45},
    {"name": "Emma", "subject": "History", "marks": 60},
    {"name": "Michael", "subject": "Math", "marks": 30},
    {"name": "Sophia", "subject": "Science", "marks": 90},
    {"name": "David", "subject": "English", "marks": 55},
    {"name": "Olivia", "subject": "History", "marks": 70},
    {"name": "Daniel", "subject": "Math", "marks": 95},
    {"name": "Grace", "subject": "Science", "marks": 50}
]

# Function to Display Students and Filter by Marks
def display_students(students):
    print("\nList of Students:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']} , Subject: {student['subject']}, Marks: {student['marks']}")
    pass_marks = int(input("Enter Pass Marks to filter students: "))
    filter_students(students, pass_marks)

# Function to Filter Students by Marks
def filter_students(students, pass_marks):
    print(f"\nStudents with marks above {pass_marks}:")
    for student in students:
        if student["marks"] >= pass_marks:
            print(f"{student['name']} - Subject: {student['subject']}, Marks: {student['marks']}")
        else:
            print(f"{student['name']} has failed in {student['subject']}")  

# Main Execution
display_students(students)
