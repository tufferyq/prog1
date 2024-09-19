"""
COMP.CS.100 Programming 1
Student: Quentin Tuffery, id: dvb366
"""

def main():

    numbers = []

    print("Give 5 numbers:")

    while len(numbers) < 5:
        number_input = int(input("Next number: "))
        numbers.append(number_input)


    print("The numbers you entered, in reverse order:")

    index = len(numbers)-1
    while index >= 0:
        print(numbers[index])
        index -= 1

if __name__ == "__main__":
    main()