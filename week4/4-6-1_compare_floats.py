# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
Programming 1
Comparing floats
"""

EPSILON = 0.000000001

def compare_floats(nb1, nb2, EPSILON):
    """
    Compare nb1 and nb2, to check if the difference is they're near (i.e if the difference is less than Epsilon)
    """
    is_equal = abs(nb1 - nb2) < EPSILON
    return is_equal