"""
COMP.CS.100 Programming 1
Project - Department, courses, credits
Author: Quentin TUFFERY, id: dvb366
"""

def read_file(filename):
    """
    Reads and saves the information from the file into a dictionary.
    :param filename: string, name of the file that contains the data
    :return: dictionary containing the department data with courses and credits
    """
    dictionary = {}

    try:
        # Attempt to open the file. If it fails, print an error and return None.
        file = open(filename, mode="r")
    except FileNotFoundError:
        print("Error opening file!")
        return

    # Read the file line by line and process each line
    for line in file:
        line = line.rstrip()  # Remove any trailing newline or whitespace
        parts = line.split(";")  # Split the line by the delimiter ";"
        try:
            department, course_name, credit_points = parts
        except ValueError:
            print("Error in file!")  # Print error if the format is incorrect
            return

        # If department is not in the dictionary, add it
        if department not in dictionary:
            dictionary[department] = {}

        # Add the course and its credits to the department
        dictionary[department][course_name] = credit_points

    file.close()  # Close the file after reading
    return dictionary

def separate_command(entered_command):
    """
    Separates the command input into its components.
    :param entered_command: string, raw input command from user
    :return: tuple (command, department, course_name, credits)
    """
    parts = entered_command.split()  # Split the input into parts by spaces
    command = parts[0].lower()  # Extract the command (always first part)

    department = None
    course_name = None
    credits = None

    if len(parts) > 1:
        department = parts[1]  # Store department, if provided, in lowercase for consistency

    if command == "d":
        # For the delete command, everything after the department is treated as part of the course name
        if len(parts) > 2:
            course_name = " ".join(parts[2:])
    elif command == "a":
        # For add command, the last part should be parsed as credits, and the rest as the course name
        if len(parts) > 3:
            credits = parts[-1]
            try:
                credits = int(credits)  # Attempt to convert to an integer
            except ValueError:
                credits = None  # If conversion fails, set credits to None
            course_name = " ".join(parts[2:-1])  # Join the parts to form the course name
        elif len(parts) == 3:
            course_name = parts[2]  # If only department and course name are given, store the course name

    elif len(parts) == 3:
        # For commands like "c" or "r" that don't involve a course name but require department
        course_name = parts[2]

    return command, department, course_name, credits

def newline():
    """
    Creates a new, empty line for better readability in output.
    """
    print()

def print_department(data, department_name):
    """
    Prints the courses and credits of the selected department.
    :param department_name: string, name of the department to list courses for
    :param data: dictionary containing the department data
    """
    try:
        # Get the list of courses in the department, sorted by course name
        keyslist = sorted(list(data[department_name].keys()))
    except KeyError:
        print('Department not found!')  # Print error if department does not exist
        return

    print(f"*{department_name}*")  # Print department name
    for course_name in keyslist:
        print(f"{course_name} : {data[department_name][course_name]} cr")  # Print each course and its credits

def print_all(data):
    """
    Prints all departments and their courses.
    :param data: dictionary containing the department data
    """
    keyslist = sorted(data.keys())  # Get a sorted list of all department names
    for department in keyslist:
        print_department(data, department)  # Print each department

def add_course(data, department, course_name, credits):
    """
    Adds a course to a department, or creates the department if it does not exist.
    :param data: dictionary, departments, courses and offered credits
    :param department: string, name of the selected department
    :param course_name: string, name of the course to add
    :param credits: int, number of credits offered by the course to add
    """
    if department not in data:
        data[department] = {}  # Create a new department if it does not exist
        print(f"Added department {department} with course {course_name}")
    else:
        print(f"Added course {course_name} to department {department}")

    data[department][course_name] = credits  # Add or update the course in the department

def delete_course(data, department, course_name=None):
    """
    Deletes a course from a department, or the department entirely if no course is specified.
    :param data: dictionary, departments, courses and offered credits
    :param department: string, name of the selected department
    :param course_name: string, name of the course to delete
    """
    if department not in data:
        print(f"Department {department} not found!")  # Error if department does not exist
        return

    if course_name:
        if course_name in data[department]:
            del data[department][course_name]  # Delete the specified course
            print(f"Department {department} course {course_name} removed.")
            if not data[department]:
                del data[department]  # Remove department if no courses are left
        else:
            print(f"Course {course_name} from {department} not found!")  # Error if course does not exist
    else:
        del data[department]  # Delete the whole department if no course name is specified
        print(f"Department {department} removed.")

def calculate_credits(data, department):
    """
    Prints the total amount of credits offered by all the courses of the selected department.
    :param data: dictionary, departments, courses and offered credits
    :param department: string, name of the selected department
    """
    credits = 0
    try:
        # Sum up all credits for the courses in the department
        keyslist = sorted(list(data[department].keys()))
    except KeyError:
        print('Department not found!')  # Error if department does not exist
        return
    for course_name in keyslist:
        credits += int(data[department][course_name])
    print(f"Department {department} has to offer {credits} cr.")

def main():
    filename = input("Enter file name: ")
    data = read_file(filename)
    while data:
        newline()
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / "
              "[Q]uit")
        entered_command = input("Enter command: ")
        command, department, course_name, credits = separate_command(entered_command)

        if command == "a" and department and course_name and credits is not None:
            add_course(data, department, course_name, credits)

        elif command == "d" and department:
            delete_course(data, department, course_name)

        elif command == "c" and department:
            calculate_credits(data, department)

        elif command == "p":
            print_all(data)

        elif command == "r" and department:
            print_department(data, department)

        elif command == "q":
            print("Ending program.")
            break

        else:
            print("Invalid command!")
            continue
if __name__ == "__main__":
    main()