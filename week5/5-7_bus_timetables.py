"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

def next_busses(time):
    """
    This function gives the next 3 busses from a given time
    :param time: int, time
    """
    timetable = [630, 1015, 1415, 1620, 1720, 2000] * 2
    value = 0
    print("The next buses leave:")
    while value < len(timetable) :
        if time <= timetable[value]:
            print(timetable[value])
            print(timetable[value+1])
            print(timetable[value+2])
            break
        elif time > timetable[-1]:
            print(timetable[0])
            print(timetable[1])
            print(timetable[2])
            break
        else:value +=1

def main():

    current_time = (int(input("Enter the time (as an integer): ")))
    next_busses(current_time)

if __name__ == "__main__":
    main()
