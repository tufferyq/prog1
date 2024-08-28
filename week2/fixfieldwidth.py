# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program gives the multiplication table from 1 to 10 for the entered number.
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4.0f}", end = "")

        print()

if __name__ == "__main__":
    main()
