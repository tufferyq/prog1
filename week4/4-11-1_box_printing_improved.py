"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing"
Student: Quentin Tuffery, id: dvb366
"""

def newline():
    """
    creates a new empty line to improve the visual rendering.
    There's no parameters
    """

    print("")

def print_box(width, height, border_mark = "#", inner_mark = " "):
    """
    defines the box
    :param height: int height of the box
    :param width: int, width of the box
    :param inner_mark: str, inner mark inside the box
    :param border_mark: str, mark for the border of the box
    """
    for current_height in range(1,height+1):
        if current_height == 1 or current_height == height:
            print(border_mark * width)
        else:
            print(border_mark, inner_mark * (width-2), border_mark, sep ="")
        current_height += 1
    newline()

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()
