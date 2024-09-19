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
    index = 1

    while len(numbers) < amount_of_numbers:

        number_input = float(input(f"Enter the time for performance {index}: "))
        numbers.append(number_input)
        index +=1

    return numbers

def main():

    times = sorted(input_to_list(5))
    del times[0]
    del times[-1]

    average = 0
    index = 0

    while index < len(times):
        average += times[index]
        index +=1
    average = average/3

    print(f"The official competition score is {average:.2f} seconds.")

if __name__ == "__main__":
    main()