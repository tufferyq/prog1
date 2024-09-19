"""
COMP.CS.100 Programming 1
Student: Quentin Tuffery, id: dvb366
"""

def input_to_list(amount_of_numbers):
    """
    This function adds an amount of numbers into a list, this amount is defined by the user.
    :param amount_of_numbers: int, amount of numbers to add into the list
    :return numbers: list, list of numbers defined by the user
    """

    numbers = []

    print(f"Enter {amount_of_numbers} numbers:")

    while len(numbers) < amount_of_numbers:
        number_input = int(input(""))
        numbers.append(number_input)

    return numbers

def main():

    amount_of_numbers = int(input("How many numbers do you want to process: "))
    numbers = input_to_list(amount_of_numbers)

    searched_number = int(input("Enter the number to be searched: "))

    times_found = 0

    for value in numbers:
        if value == searched_number:
            times_found += 1

    if times_found > 0:
        print(f"{searched_number} shows up {times_found} times among the numbers you have entered.")
    else:
        print(f"{searched_number} is not among the numbers you have entered.")

if __name__ == "__main__":
    main()