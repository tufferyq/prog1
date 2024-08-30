# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program gives the multiplication table from 1 to 10 for the entered number.
"""

def main():

    counter = 0

    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            nbdays = 31
        elif month in [4, 6, 9, 11]:
            nbdays = 30
        elif month == 2:
            nbdays = 28

        for day in range(1, nbdays+1):
            if (counter-2) % 7 == 0:
                print(f"{day}.{month}.", end="\n")
            counter += 1
            day += 1
        month +=1


if __name__ == "__main__":
    main()
