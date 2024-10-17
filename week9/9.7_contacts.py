"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the infos from the file in a dictionary
    :param filename: name of the file that contains the data
    :return dictionary: dictionary
    """

    dictionary = {}

    file = open(filename, mode="r")
    next(file)
    for line in file:
        # If the input row was correct, it contained two parts:
        # · the show name before semicolon (;) and
        # · comma separated list of genres after the semicolon.
        # If we know that a function (method split in this case)
        # returns a list containing two elements, we can assign
        # names for those elements as follows:

        line = line.rstrip()
        parts = line.split(";")
        key, name, phone, email, skype = parts

        key = {}
        key["name"] = name
        key["phone"] = phone
        key["email"] = email
        key["skype"] = skype

        dictionary[parts[0]] = key

    file.close()
    return dictionary


def main():
    infos = read_file("/Users/qtuffery/prog1/week9/contacts.csv")
if __name__ == "__main__":
    main()