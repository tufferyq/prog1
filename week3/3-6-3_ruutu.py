"""
COMP.CS.100 Programming 1
Template for task: box printing
"""

def print_box(width,height,mark):
    """
    :param w: int, width of the box
    :param h: int, height of the box
    :param m: string, print mark
    """
    for currentheight in range(1,height+1):
        print(mark * width)
        currentheight += 1

def main():
    """
    This is the description of the function.
    """
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = str(input("Enter a print mark: "))

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
