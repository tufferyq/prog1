# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program asks the user if they're bored, until they are. When they are, the program stops.
"""


def main():
    # If the program had some other tasks to perform
    # the commands for them would be written here.

    program = True
    answer = input("Answer Y or N: ")

    while program :
        if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
            print("You answered", answer)
            program = False
        else :
            print("Incorrect entry.")
            answer = input("Answer Y or N: ")

if __name__ == "__main__":
    main()