"""
COMP.CS.100 Programming 1
Number sequences
Student: Quentin Tuffery, id: dvb366
"""

def main():

    for number in range(0,101,2):
        print(number)
        number += 1

    for number in range(100,-1,-2):
        print(number)
        number -= 1

if __name__ == "__main__":
    main()