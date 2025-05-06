# Welcome message
print("Welcome to the Student Data Organizer!")

# List to store student dictionaries
students = []

# Infinite loop for menu
while True:
    # Display menu options
    print("\nSelect an Option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    # Take user input for menu choice
    choice = input("Enter choice: ")

    match choice:

        # Option 1: Add a new student
        case "1":
            print("\nEnter Student Details")

            # Take student details from user
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            # Create student dictionary
            student = {
                "ID": student_id,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": subjects
            }

            # Add student to list
            students.append(student)
            print("Student added successfully!")

        # Option 2: Display all students
        case "2":
            print("\nAll Students:")
            if not students:
                print("No students available.")
            else:
                for s in students:
                    print(s)

        # Option 3: Update student information
        case "3":
            update_id = int(input("Enter Student ID to update: "))
            found = False

            for student in students:
                if student["ID"] == update_id:
                    found = True
                    print("What do you want to update?")
                    print("1. Name")
                    print("2. Age")
                    print("3. Grade")
                    print("4. DOB")
                    print("5. Subjects")
                    print("6. All fields")
                    field_choice = input("Enter your choice: ")

                    match field_choice:
                        case "1":
                            name = input("Enter new name: ")
                            student["Name"] = name
                        case "2":
                            age = int(input("Enter new age: "))
                            student["Age"] = age
                        case "3":
                            grade = input("Enter new grade: ")
                            student["Grade"] = grade
                        case "4":
                            dob = input("Enter new DOB (YYYY-MM-DD): ")
                            student["DOB"] = dob
                        case "5":
                            subjects = input("Enter new subjects (comma-separated): ")
                            student["Subjects"] = subjects
                        case "6":
                            student["Name"] = input("Enter new name: ")
                            student["Age"] = int(input("Enter new age: "))
                            student["Grade"] = input("Enter new grade: ")
                            student["DOB"] = input("Enter new DOB (YYYY-MM-DD): ")
                            student["Subjects"] = input("Enter new subjects (comma-separated): ")
                        case _:
                            print("Invalid choice for update.")
                    print("Student information updated.")
                    break

            if not found:
                print("Student not found.")

        # Option 4: Delete a student
        case "4":
            delete_id = int(input("Enter Student ID to delete: "))
            found = False

            for i in range(len(students)):
                if students[i]["ID"] == delete_id:
                    found = True
                    del students[i]
                    print("Student deleted successfully.")
                    break

            if not found:
                print("Student not found.")

        # Option 5: Display Subjects Offered
        case "5":
            all_subjects = set()
            for student in students:
                subject_list = [sub.strip() for sub in student["Subjects"].split(",")]
                all_subjects.update(subject_list)

            if all_subjects:
                print("\nSubjects Offered:")
                for subject in sorted(all_subjects):
                    print(subject)
            else:
                print("No subjects found. Please add students first.")

        # Option 6: Exit
        case "6":
            print("Exiting program.")
            break

        # Invalid input
        case _:
            print("Invalid choice. Please enter a valid option.")
