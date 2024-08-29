# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program asks the user if they're bored, until they are. When they are, the program stops.
"""


def main():
    # If the program had some other tasks to perform
    # the commands for them would be written here.

    answer = "n"

    while answer != "y":
        answer = input("Bored? (y/n) ")

    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()