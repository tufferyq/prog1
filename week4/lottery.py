# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
Programming 1
Lottery probabilities
"""
def check(total_balls, drawn_balls):
    """
    checks if the nb entered is > 0, and if nb of drawn balls < nb of total balls
    If ok, it prints the result
    """
    check_status = False
    if total_balls <= 0 or drawn_balls <= 0:
        print("The number of balls must be a positive number.")
    elif drawn_balls > total_balls:
        print("At most the total number of balls can be drawn.")
    else:
        check_status = True
    if check_status:
        factorial_result = factorial(total_balls) / (factorial (total_balls - drawn_balls) * factorial(drawn_balls))
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/{factorial_result:.0f}")

def factorial(number, result=1):
    """
    calculates the factorial of the entered number
    """
    for i in range (1, number+1):
        result *= i
    return result

def main():

    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    check(total_balls, drawn_balls)

if __name__ == "__main__":
    main()
