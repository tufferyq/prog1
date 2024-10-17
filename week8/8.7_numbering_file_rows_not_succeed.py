"""
COMP.CS.100 - Programming 1
Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""


def main():
    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode = 'r')

    except FileNotFoundError:
        print("There was an error in reading the file.")
        return

    index = 1
    for file_line in file:
        file_line = file_line.rstrip()
        print(f"{index} {file_line}")
        index +=1

    file.close()


if __name__ == "__main__":
    main()