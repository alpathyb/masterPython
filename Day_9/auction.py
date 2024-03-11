import logo

print(logo.logo)
print("Welcome to the secret Auction Program.")

bidders = []  # to stores the bidders
is_continue = True


def clear():
    print("\n" * 20)


while is_continue:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))

    bidders.append(
        {
            name: bid
        }
    )

    ask_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if ask_continue == "no":
        max_bid = float('-inf')
        max_name = ""
        is_continue = False
        for dictionary in bidders:
            for name, bid in dictionary.items():
                if bid > max_bid:
                    max_bid = bid
                    max_name = name

        print(f"the winner is {max_name} with ${max_bid} bid")
    else:
        clear()
