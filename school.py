#!/usr/bin/env python3

# ##############################################################################
# Written with Claude code, using the prompt:
#
# Write a python CLI application that manages a school's student and course inventory.
# When run, it should drop the user into a repl loop that supports the following commands -
# * help prints out all available commands with a short description
# * list courses - lists al available courses
# * add course - adds a new course to available courses
# * list students - lists all the students
# * add student - adds a student, given their name and grade
# * take course - add a course to a students list of courses
# * drop course - removes a course from a students list of courses
# * quit school - remove all courses for a student
# * student details - list student's name, grade and the courses they are taking
# * course details - list all students (name + grade) that are taking the course
#
# The implementation should use no classes, instead use global variables and arrays
# with primitive types to store all information - an array of strings for student names,
# and array of strings for student grades and so on, where the matching indices in
# the different arrays correspond to each other (i.e. the 2nd entry in the
# student_names array and student_grades array are for the same student etc.)
#
# Do make heavy use of functions to split up the code.
#
# Remember, DO NOT USE CLASSES, DICTIONARY or any other object types.
# ##############################################################################

# Global data structures - using parallel arrays
student_names = []
student_grades = []
courses = []
# For enrollments: parallel arrays where each entry corresponds to a student
# Each entry is a list of course indices
student_course_indices = []

def print_help():
    """Print all available commands"""
    print("\n=== Available Commands ===")
    print("help                - Show this help message")
    print("list courses        - List all available courses")
    print("add course          - Add a new course")
    print("list students       - List all students")
    print("add student         - Add a new student")
    print("take course         - Enroll a student in a course")
    print("drop course         - Remove a course from a student")
    print("quit school         - Remove all courses for a student")
    print("student details     - Show student information and their courses")
    print("course details      - Show all students enrolled in a course")
    print("exit                - Exit the program")
    print("==========================\n")

def list_courses():
    """List all available courses"""
    if len(courses) == 0:
        print("No courses available.")
        return

    print("\n=== Available Courses ===")
    for i in range(len(courses)):
        print(f"{i + 1}. {courses[i]}")
    print()

def add_course():
    """Add a new course"""
    course_name = input("Enter course name: ").strip()

    if len(course_name) == 0:
        print("Course name cannot be empty.")
        return

    # Check for duplicates
    for i in range(len(courses)):
        if courses[i].lower() == course_name.lower():
            print(f"Course '{course_name}' already exists.")
            return

    courses.append(course_name)
    print(f"Course '{course_name}' added successfully.")

def list_students():
    """List all students"""
    if len(student_names) == 0:
        print("No students enrolled.")
        return

    print("\n=== Students ===")
    for i in range(len(student_names)):
        print(f"{i + 1}. {student_names[i]} (Grade {student_grades[i]})")
    print()

def add_student():
    """Add a new student"""
    name = input("Enter student name: ").strip()

    if len(name) == 0:
        print("Student name cannot be empty.")
        return

    grade = input("Enter student grade: ").strip()

    if len(grade) == 0:
        print("Grade cannot be empty.")
        return

    student_names.append(name)
    student_grades.append(grade)
    student_course_indices.append([])  # Empty list of course indices

    print(f"Student '{name}' (Grade {grade}) added successfully.")

def find_student_index(name):
    """Find student index by name (case-insensitive)"""
    for i in range(len(student_names)):
        if student_names[i].lower() == name.lower():
            return i
    return -1

def find_course_index(course_name):
    """Find course index by name (case-insensitive)"""
    for i in range(len(courses)):
        if courses[i].lower() == course_name.lower():
            return i
    return -1

def take_course():
    """Enroll a student in a course"""
    if len(student_names) == 0:
        print("No students available. Add students first.")
        return

    if len(courses) == 0:
        print("No courses available. Add courses first.")
        return

    student_name = input("Enter student name: ").strip()
    student_idx = find_student_index(student_name)

    if student_idx == -1:
        print(f"Student '{student_name}' not found.")
        return

    course_name = input("Enter course name: ").strip()
    course_idx = find_course_index(course_name)

    if course_idx == -1:
        print(f"Course '{course_name}' not found.")
        return

    # Check if student is already enrolled
    enrolled_courses = student_course_indices[student_idx]
    for i in range(len(enrolled_courses)):
        if enrolled_courses[i] == course_idx:
            print(f"Student '{student_names[student_idx]}' is already enrolled in '{courses[course_idx]}'.")
            return

    student_course_indices[student_idx].append(course_idx)
    print(f"Student '{student_names[student_idx]}' enrolled in '{courses[course_idx]}'.")

def drop_course():
    """Remove a course from a student"""
    if len(student_names) == 0:
        print("No students available.")
        return

    student_name = input("Enter student name: ").strip()
    student_idx = find_student_index(student_name)

    if student_idx == -1:
        print(f"Student '{student_name}' not found.")
        return

    course_name = input("Enter course name: ").strip()
    course_idx = find_course_index(course_name)

    if course_idx == -1:
        print(f"Course '{course_name}' not found.")
        return

    # Find and remove the course from student's enrollments
    enrolled_courses = student_course_indices[student_idx]
    found = False
    for i in range(len(enrolled_courses)):
        if enrolled_courses[i] == course_idx:
            enrolled_courses.pop(i)
            found = True
            break

    if found:
        print(f"Course '{courses[course_idx]}' dropped for student '{student_names[student_idx]}'.")
    else:
        print(f"Student '{student_names[student_idx]}' is not enrolled in '{courses[course_idx]}'.")

def quit_school():
    """Remove all courses for a student"""
    if len(student_names) == 0:
        print("No students available.")
        return

    student_name = input("Enter student name: ").strip()
    student_idx = find_student_index(student_name)

    if student_idx == -1:
        print(f"Student '{student_name}' not found.")
        return

    course_count = len(student_course_indices[student_idx])
    student_course_indices[student_idx] = []

    print(f"All {course_count} course(s) removed for student '{student_names[student_idx]}'.")

def student_details():
    """Show detailed information about a student"""
    if len(student_names) == 0:
        print("No students available.")
        return

    student_name = input("Enter student name: ").strip()
    student_idx = find_student_index(student_name)

    if student_idx == -1:
        print(f"Student '{student_name}' not found.")
        return

    print(f"\n=== Student Details ===")
    print(f"Name: {student_names[student_idx]}")
    print(f"Grade: {student_grades[student_idx]}")
    print(f"Courses:")

    enrolled_courses = student_course_indices[student_idx]
    if len(enrolled_courses) == 0:
        print("  No courses enrolled")
    else:
        for i in range(len(enrolled_courses)):
            course_idx = enrolled_courses[i]
            print(f"  - {courses[course_idx]}")
    print()

def course_details():
    """Show all students enrolled in a course"""
    if len(courses) == 0:
        print("No courses available.")
        return

    course_name = input("Enter course name: ").strip()
    course_idx = find_course_index(course_name)

    if course_idx == -1:
        print(f"Course '{course_name}' not found.")
        return

    print(f"\n=== Course Details ===")
    print(f"Course: {courses[course_idx]}")
    print(f"Enrolled Students:")

    # Find all students enrolled in this course
    enrolled_students = []
    for i in range(len(student_names)):
        student_courses = student_course_indices[i]
        for j in range(len(student_courses)):
            if student_courses[j] == course_idx:
                enrolled_students.append(i)
                break

    if len(enrolled_students) == 0:
        print("  No students enrolled")
    else:
        for i in range(len(enrolled_students)):
            student_idx = enrolled_students[i]
            print(f"  - {student_names[student_idx]} (Grade {student_grades[student_idx]})")
    print()

def process_command(command):
    """Process a user command"""
    cmd = command.strip().lower()

    if cmd == "help":
        print_help()
    elif cmd == "list courses":
        list_courses()
    elif cmd == "add course":
        add_course()
    elif cmd == "list students":
        list_students()
    elif cmd == "add student":
        add_student()
    elif cmd == "take course":
        take_course()
    elif cmd == "drop course":
        drop_course()
    elif cmd == "quit school":
        quit_school()
    elif cmd == "student details":
        student_details()
    elif cmd == "course details":
        course_details()
    elif cmd == "exit":
        return False
    else:
        print(f"Unknown command: '{command}'. Type 'help' for available commands.")

    return True

def main():
    """Main REPL loop"""
    print("=" * 50)
    print("Welcome to the School Management System")
    print("=" * 50)
    print("Type 'help' to see available commands\n")

    running = True
    while running:
        try:
            command = input("school> ").strip()
            if len(command) > 0:
                running = process_command(command)
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            print("\n\nExiting...")
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()
