# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
This program gives the multiplication table from 1 to 10 for the entered number.
"""

def main():

    previous_fib = 1
    current_fib = 1

    number = int(input("How many Fibonacci numbers do you want? "))

    for stage in range(1, number+1):
        if stage <= 2:
            print(f"{stage}. 1")
        else:
            next_fib = previous_fib + current_fib
            print(f"{stage}. {next_fib}")
            previous_fib = current_fib
            current_fib = next_fib


if __name__ == "__main__":
    main()
