def main():
    amount = 50
    print("Amount due: ", amount)

    while True:

        money = int(input("Insert Coin: "))

        if money == 25 or money==10 or money==5:
            amount = amount - money

        if amount <= 0:
                print("Change Owed:", abs(amount))
                break

        print("Amount Due:", amount)

main()





# def main():
#     amount_due = 0
#     accepted_coins = {25: "25 cents", 10: "10 cents", 5: "5 cents"}

#     while amount_due < 50:
#         coin = input("Insert Coin: ")
#         coin = int(coin) if coin.isdigit() else 0

#         if coin in accepted_coins:
#             amount_due = 50 - coin
#             print(f"Amount Due: {amount_due}")
#         else:
#             print("Amount Due: 50")

#     change_owed = amount_due - 50
#     if change_owed > 0:
#         print(f"Change Owed: {change_owed}")
#     elif change_owed == 0:
#         print("Change Owed: 0")


# if __name__ == "__main__":
#     main()











# def main():
#     amount_due = 0
#     change_owed = 0
#     accepted_coins = [25, 10, 5]

#     while amount_due < 50:
#         coin = input("Insert Coin: ")
#         coin = int(coin) if coin.isdigit() else 0

#         if coin in accepted_coins:
#             amount_due = 50-coin
#             print("Amount Due:", amount_due)
#         else:
#             print("Amount Due: 50")

#     change_owed = amount_due - 50
#     print("Change Owed:", change_owed)

# if __name__ == "__main__":
#     main()









# def main():
#     amount_due = 0
#     accepted_coins = {25: "25 cents", 10: "10 cents", 5: "5 cents"}

#     while amount_due < 50:
#         coin = input("Insert Coin: ")
#         coin = int(coin) if coin.isdigit() else 0

#         if coin in accepted_coins:
#             amount_due= 50-coin
#             print(f"Amount Due: {amount_due}")
#         else:
#             print("Amount Due: 50")

#     change_owed = amount_due - 50
#     print(f"Change Owed: {change_owed}")

# if __name__ == "__main__":
#     main()









