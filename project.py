# Student GPA Management System
import os

courses = []
student_id = []
student = ""
credit = 0
average_gpa = 0

# Adding student information (completed)
def adding_info():
    global student_id, student, credit, courses, average_gpa

    student_id = int(input("Enter student ID: "))
    student = input("Enter student name: ")
    n = int(input("How many courses? "))

    for i in range(n):

        name = input(f"Enter course {i+1} name: ")

        score = float(input(f"Enter score for {name}: "))
        while score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
            score = float(input(f"Enter score for {name}: "))

        credit = float(input(f"Enter credit for {name}: "))
        while credit <= 0:
            print("Invalid credit. Please enter a positive number.")
            credit = float(input(f"Enter credit for {name}: "))

        if score >= 93:
            gpa = credit*4.0
        elif score >= 90:
            gpa = credit*3.8
        elif score >= 87:
            gpa = credit*3.25
        elif score >= 83:
            gpa = credit*3.0
        elif score >= 80:
            gpa = credit*2.75
        elif score >= 77:
            gpa = credit*2.25
        elif score >= 73:
            gpa = credit*2.0
        else:
            gpa = credit*1.0

        courses.append({"name": name, "score": score,
                       'gpa': gpa, 'credit': credit})

    average_gpa = sum(course["gpa"] for course in courses) / sum(course["credit"] for course in courses)

    print_info()
    save_info()


# Print the table (completed)
def print_info():
    print("\n" + "=" * 40)
    print("Student Information:")
    print(f"Student ID:{student_id} ")
    print(f"Student Name:{student} ")
    print(f"\n{'Course':<20} {'Score'}")
    print("-" * 28)
    for course in courses:
        print(f"{course['name']:<20} {course['score']}")
    print(f"Average GPA: {average_gpa:.2f}\n")


# Save the information to a text file (completed)
def save_info():
    with open("student_info.txt", "a") as file:
        file.write( "=" * 40 + "\n")
        file.write("Student Information:\n")
        file.write(f"Student ID: {student_id}\n")
        file.write(f"Student Name: {student}\n")
        file.write(f"\n{'Course':<20} {'Score'}\n")
        file.write("-" * 28 + "\n")
        for course in courses:
            file.write(f"{course['name']:<20} {course['score']}\n")
        file.write(f"Average GPA: {average_gpa:.2f}\n")


# Read the information in the student_info.text (completed)
def read_info():
    if not os.path.exists("student_info.txt"):
        print("File not found")
        return None
    
    with open("student_info.txt", "r") as file:
        content = file.read()
    
    block = content.split( "=" * 40 + "\n")
    return block

# Searching student information from student_info.text (completed)
def search_info():
    info_blocks = read_info()
    if not info_blocks:
        Print("File not found")
        return
    
    search_id = input("Enter student ID to search: ")
    for block in info_blocks:
        if f"Student ID: {search_id}\n" in block:
            print(' ')
            print("=" * 40)
            print(block)
            return

    print("Student information not found.")

def remove_info():
    info_blocks = read_info()
    if not info_blocks:
        print("File not found")
        return
    
    remove_id = input("Enter student ID to replace: ")

    new_blocks = []
    removed = False

    for block in info_blocks:
        if f"Student ID: {remove_id}\n" in block:
            removed = True
        else:
            new_blocks.append(block)

    if not removed:
        print("Student not found")
        return
    
    with open("student_info.txt", "w") as file:
        for block in new_blocks:
            if block.strip():
                file.write("="*40+"\n")
                file.write(block)
     
    print(f"Student information of ID: {remove_id} removed succesfully")
            

# Menu (completed)
while True:
    print("\nWelcome to the Student GPA Management System!"
        "\nPlease choose an option:\n1. Add student information."
        "\n2. Remove student information."
        "\n3. Search student information."
        "\n4. Exit.")

    choice = input("Enter your choice (1/2/3/4): ")

    while choice not in ['1', '2', '3', '4']:

        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        adding_info()

    elif choice == '2':
        remove_info()

    elif choice == '3':
        search_info()

    elif choice == '4':
        print("Exiting the program. See you next time!")
        break
