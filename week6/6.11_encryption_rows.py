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

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    result = ""

    if text.casefold() not in regular_chars:
        result += text

    elif text.isupper():
        encryption_index = regular_chars.index(text.casefold())
        result += encrypted_chars[encryption_index].upper()

    else:
        encryption_index = regular_chars.index(text)
        result += encrypted_chars[encryption_index]

    return result

def row_encryption(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    row_encrypted = ""
    characters = list(text)

    for index in range(len(characters)):
        row_encrypted += encrypt(characters[index])

    return row_encrypted

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for index in range(len(msg)):
        print(row_encryption(msg[index]))



if __name__ == "__main__":
    main()
