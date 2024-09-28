"""
COMP.CS.100 Programming 1
Code Template
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
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for index in range(len(msg)):
        print(msg[index].upper())



if __name__ == "__main__":
    main()
