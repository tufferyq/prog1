"""
COMP.CS.100 - Programming 1
Project Week 6 - Levels changes in seawater

Based on a list of values given by the user, this program automatically
calculates the:
- minimum value
- maximum value
- median
- mean (average)
- deviation

Author: Quentin Tuffery
    id: dvb366
    email: quentin.tuffery@tuni;fi
"""

def newline(amount):
    """
    prints a certain amount of blank lines on the screen
    :param amount: int, number of blank lines to print
    """
    for index in range (0,amount):
        print("")
        index +=1

def list_construction():
    """
    This function allows us to build the list of values we will use in the
    rest of the program
    :return values: list of N values
    """
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    values = []
    new_value = 0

    # Adds the new value to the list, if the line is not empty.
    while new_value != "":
        new_value = input()
        if new_value != "":
            values.append(float(new_value))

    return values

def list_check(list):
    """
    This function will check that the list has at least 2 values.
    If not, it will return play_program = False, which will stop the program.
    :param list: list, list of numbers
    :return play_program: bool, it will return True only if there are more than
    two values in the list
    """
    if len(list) < 2:
        print("Error: At least two measurements must be entered!")
        play_program = False
    else : play_program = True
    return play_program

def minimum(list):
    """
    this function will return the minimum value of the list
    :param list: list, list of numbers
    :return result: float, minimum value of the list
    """
    result = min(list)
    return result

def maximum(list):
    """
    this function will return the maximum value of the list
    :param list: list, list of numbers
    :return result: float, maximum value of the list
    """
    result = max(list)
    return result

def median(list):
    """
    this function will return the median value of the list
    :param list: list, list of numbers
    :return result: float, median value of the list
    """
    #sorts the list
    list = sorted(list)

    #two cases, if the amount of values is even or odd
    #case 1 : even
    if len(list) % 2 == 0:
        median_value1 = int((len(list)/2)-1)
        median_value2 = int(len(list)/2)
        result = mean([list[median_value1],list[median_value2]])
    #case 2 : odd
    else:
        median_value = int(len(list)/2)
        result = list[median_value]

    return result

def mean(list):
    """
    this function will return the mean (average) of the list
    :param list: list, list of numbers
    :return result: float, mean of the list
    """
    result = 0
    #adds up all the values of the list
    for index in range(0,len(list)):
        result += list[index]
        #and divides the result by the amount of values of the list
    result = result/len(list)
    return result

def deviation(list):
    """
    this function will return the deviation value of the list
    :param list: list, list of numbers
    :return result: float, deviation value of the list
    """
    result = 0
    #calculating the second part of the variance (the sum part)
    for index in range (0,len(list)):
        result += (list[index] - mean(list)) ** 2
        index += 1
    # then, calculating the variance
    result = 1/(len(list)-1) * result
    #finally, calculating the square root of the deviation, which is actually the deviation
    result = result ** (1/2)
    return result

def main():
    measurements = list_construction()
    play_program = list_check(measurements)

    if play_program is True:
        newline(3)
        print(f"Minimum:    {minimum(measurements):.2f} cm")
        print(f"Maximum:    {maximum(measurements):.2f} cm")
        print(f"Median:     {median(measurements):.2f} cm")
        print(f"Mean:       {mean(measurements):.2f} cm")
        print(f"Deviation:  {deviation(measurements):.2f} cm")

if __name__ == "__main__":
    main()