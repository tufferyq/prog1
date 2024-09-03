# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(a,b,c):
    """
    defines the area of the triangle
    :param a: int, 1st side of the triangle
    :param b: int, 2nd side of the triangle
    :param c: int, 3rd side of the triangle
    """
    s = (a+b+c)/2
    result = sqrt(s*(s-a)*(s-b)*(s-c))
    return result

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {area(a,b,c):.1f}")

if __name__ == "__main__":
    main()
