# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""

def read_input(string):
    """
    To check the input value (>0)
    """
    value = int(input(string))
    while value <= 0:
        value = int(input(string))
    return value

def print_box(w,h,m):
    """
    This function allow the program to print the box
    :param w: int, width of the box
    :param h: int, height of the bow
    :param m: string, mark used to create the box
    """
    for currentheight in range(1,h+1):
        print(m * w)
        currentheight += 1

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print("")
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
