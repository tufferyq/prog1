"""
The price of a single ride bus ticket in Tampere
and surrounding areas on Aug 23rd, 2020.

The rules used by the program are:

  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00

Limited usefulness, the actual rules are more complex.
"""

def main():
    string = input("Please, enter your age: ")
    age = int(string)

    if age >= 25:
        ticket_price = 2.04
    elif age >= 17 and age <= 24:
        ticket_price = 1.47
    elif age >= 7 and age <= 16:
        ticket_price = 1.02
    elif age >= 0 and age <= 6:
        ticket_price = 0.00

    print("Your ride will cost:",ticket_price)


if __name__ == "__main__":
    main()