# This program prompts the user to insert a coin, one at a time, each time
# informing the user of the amount due. Once the user has inputted at least 50
# cents. Lastly, it outputs how many cents in change the user is owed.

amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            change_owed = abs(amount_due)
            print(f"Change Owed: {change_owed}")
    else:
        print(f"Amount Due: {amount_due}")