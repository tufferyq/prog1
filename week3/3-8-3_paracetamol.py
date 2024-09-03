# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(weight, time, total_doze_24):
    """
    This function defines the amount of paracetamol that a person can take right now.
    :param weight: int, weight of the person
    :param time: int, time since last dose of paracetamol
    :param total_doze_24: total amount paracetamol taken for the last 24hrs
    """
    max_per_kg = 15 * weight
    MAX_PER_DAY = 4000

    if time >= 6:
        if max_per_kg < MAX_PER_DAY - total_doze_24:
            dose = max_per_kg
        elif max_per_kg >= MAX_PER_DAY - total_doze_24:
            dose = MAX_PER_DAY - total_doze_24
    else: dose = 0
    return dose

def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight,time,total_doze_24)}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
