# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program gives the multiplication table for the entered number, until the last result gets above 100
"""

def main():
    # If the program had some other tasks to perform
    # the commands for them would be written here.

    number = int(input("Choose a number: "))
    factor = 1

    result = factor * number
    print(factor, "*", number, "=", result)
    factor += 1

    while result  < 100:
        result = factor * number
        print(factor, "*", number, "=", result)
        factor += 1

if __name__ == "__main__":
    main()