# author : Quentin Tuffery
# Student id : dvb366

amount_study_benefit = float(input("Enter the amount of the study benefits: "))
amount_raised1 = amount_study_benefit * 1.0117
amount_raised2 = amount_raised1 * 1.0117

print("If the index raise is 1.17 percent, the study benefit,");
print("after a raise, would be",amount_raised1, "euros");
print("and if there was another index raise, the study");
print("benefits would be as much as",amount_raised2,"euros")