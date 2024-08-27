# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

def main():

    string = input("Purchase price: ")
    purchase_price = int(string)

    string = input("Paid amount of money: ")
    paid_amount = int(string)

    total_change = paid_amount - purchase_price

    change_ten = total_change // 10
    remaining_change = total_change % 10
    change_five = remaining_change // 5
    remaining_change = remaining_change % 5
    change_two = remaining_change // 2
    remaining_change = remaining_change % 2
    change_one = remaining_change

    if total_change <= 0:
        print("No change")

    if total_change > 0:
        print("Offer change: ")
        if change_ten >0:
            print(change_ten, "ten-euro notes")
        if change_five >0:
            print(change_five, "five-euro notes")
        if change_two >0:
            print(change_two, "two-euro coins")
        if change_one >0:
            print(change_one, "one-euro coins")

if __name__ == "__main__":
    main()