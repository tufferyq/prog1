# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program gives the multiplication table from 1 to 10 for the entered number.
"""

def main():
    # If the program had some other tasks to perform
    # the commands for them would be written here.

    end = int(input("How many numbers would you like to have? "))

    for i in range(1,end+1):
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")
            i += 1
        elif i % 3 == 0:
            print("zip")
            i += 1
        elif i % 7 ==0:
            print("boing")
            i += 1
        else :
            print(i)
            i += 1

if __name__ == "__main__":
    main()