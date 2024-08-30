# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program gives the multiplication table from 1 to 10 for the entered number.
"""

def main():
    # If the program had some other tasks to perform
    # the commands for them would be written here.

    number = int(input("Choose a number: "))
    factor = 1

    while factor <=10:
        result = factor * number
        print(factor, "*", number, "=", factor * number)
        factor += 1

if __name__ == "__main__":
    main()