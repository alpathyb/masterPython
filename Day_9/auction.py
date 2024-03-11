import logo

print(logo.logo)
print("Welcome to the secret Auction Program.")

bidders = {}  # to stores the bidders
is_continue = True


def clear():
    print("\n" * 20)


while is_continue:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))

    bidders[name] = bid

    ask_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if ask_continue == "no":
        max_bid = 0
        max_name = ""
        is_continue = False
        for name_bid, value in bidders.items():
            if value > max_bid:
                max_bid = value
                max_name = name_bid

        print(f"the winner is {max_name} with ${max_bid} bid")
    else:
        clear()
