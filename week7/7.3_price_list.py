"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    program = True

    while program:

        product = input("Enter product name: ")
        # remove spaces from the string
        product = product.replace(" ", "")

        #if empty, stop program
        if product == "":
            print("Bye!")
            program = False

        #if not in list, send error and repeat program
        elif product not in PRICES:
            print(f"Error: {product} is unknown.")

        else :
            print(f"The price of {product} is {PRICES[product]:.2f} e")

if __name__ == "__main__":
    main()