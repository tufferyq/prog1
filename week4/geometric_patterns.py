"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
Student: Quentin Tuffery, id: dvb366
"""

from math import pi

def side(figure):
    """
    checks if the values of sides entered are positive values
    """
    if figure == "s":
        side = float(input("Enter the length of the square's side: "))
        while side <= 0:
            side = float(input("Enter the length of the square's side: "))
        return side
    if figure == "r":
        side1 = float(input("Enter the length of the rectangle's side 1: "))
        while side1 <= 0:
            side1 = float(input("Enter the length of the rectangle's side 1: "))
        side2 = float(input("Enter the length of the rectangle's side 2: "))
        while side2 <= 0:
            side2 = float(input("Enter the length of the rectangle's side 2: "))
        return side1, side2
    if figure == "c":
        radius = float(input("Enter the circle's radius: "))
        while radius <= 0:
            radius = float(input("Enter the circle's radius: "))
        return radius

def s_circumference(side):
    """
    calculates the circumference of squares
    :param side: int, length of a square side
    """
    return side * 4

def s_surface(side):
    """
    calculates the surface of squares
    :param side: int, length of a square side
    """
    return side ** 2
def r_circumference(side1,side2):
    """
    calculates the circumference of rectangles
    :param side1: int, length of 1st side
    :param side2: int, length of 2nd side
    """
    return (side1+side2)*2

def r_surface(side1,side2):
    """
    calculates the surface of rectangles
    :param side1: int, length of 1st side
    :param side2: int, length of 2nd side
    """
    return side1 * side2

def c_circumference(radius):
    """
    calculates the circumference of circles
    :param radius: int, the radius of the circle
    """
    return 2 * radius * pi

def c_surface(radius):
    """
    calculates the surface of circles
    :param radius: int, the radius of the circle
    """
    return radius ** 2 * pi

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            # with square.
            sidevalue = side(answer)
            print(f"The circumference is "
                  f"{s_circumference(sidevalue):.2f}")
            print(f"The surface area is {s_surface(sidevalue):.2f}")

        elif answer == "r":
            # with rectangle.
            side1, side2 = side(answer)
            print(f"The circumference is {r_circumference(side1, side2):.2f}")
            print(f"The surface area is {r_surface(side1, side2):.2f}")

        elif answer == "c":
            # with circle.
            radius = side(answer)
            print(f"The circumference is "
                  f"{c_circumference(radius):.2f}")
            print(f"The surface area is {c_surface(radius):.2f}")

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
