"""
COMP.CS.100 Programming 1
Student: Quentin Tuffery, id: dvb366
"""

def are_all_members_same(list):
    """
    This function adds an amount of numbers into a list, this amount is defined by the user.
    :param list: list, list of numbers
    :return truthness: bool, true if all numbers of the list are the same
    """
    index = 1
    result = True

    while index < len(list):
        result = list[0] == list[index]
        if not result:
            break
        index +=1
    return result
