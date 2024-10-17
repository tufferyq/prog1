"""
COMP.CS.100 - Programming 1
Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""

def read_message():
    """
    Saves the multiples rows of message into one list
    :return list: list of strings, rows of messages given by the user
    """
    list = []
    message = str(0)

    while message != "":
        message = input("")
        if message != "":
            list.append(str(message))

    return list

def main():
    filename = input("Enter the name of the file: ")

    try:
        write_file = open(filename, mode = 'w')

        print("Enter rows of text. Quit by entering an empty row.")

        text = read_message()

        for index in range(len(text)):
            print(f"{index+1} {text[index]}", file = write_file)

    except:
        print(f"Writing the file {filename} was not successful.")
        return

    print(f"File {filename} has been written.")

    write_file.close()


if __name__ == "__main__":
    main()