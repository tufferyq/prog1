# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program asks the user if they're bored, until they are. When they are, the program stops.
"""

def main():
    # If the program had some other tasks to perform
    # the commands for them would be written here.

    yes_letters = ["y", "Y"]
    no_letters = ["n", "N"]
    program = True

    answer = input("Bored? (y/n) ")

    while answer not in yes_letters :
        while program is True:
            if answer in no_letters :
                answer = input("Bored? (y/n) ")
                continue
            elif answer in yes_letters:
                program = False
            else:
                print("Incorrect entry.")
                answer = input("Bored? (y/n) ")
                continue
    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()