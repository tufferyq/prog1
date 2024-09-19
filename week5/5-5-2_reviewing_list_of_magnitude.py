"""
COMP.CS.100 Programming 1
Student: Quentin Tuffery, id: dvb366
"""

def is_the_list_in_order(list):
    """
    This function checks that the numbers of the list are in the correct order.
    :param list: list, list of numbers
    :return result: bool, true if the numbers of the list are in order
    """
    result = True

    if len(list) == 0 or len(list) == 1:
        return True

    result = list == sorted(list)
    return result
