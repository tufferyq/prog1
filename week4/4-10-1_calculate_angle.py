"""
COMP.CS.100 Programming 1
Triangles angles calculation
Student: Quentin Tuffery, id: dvb366
"""



def calculate_angle(angle1=90, angle2=90):
    """
    calculates the 3rd angle depending of the 2 other angles
    """
    result = 180 - angle1 - angle2
    return result