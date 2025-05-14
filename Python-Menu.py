import os, sys

#--- Class ---#
class Consumer:
    def __init__(self, money: int, items_in_cart: list, amount_added_up = int, index = int, has_purchased_fries = bool, has_purchased_beverage = bool, has_purchased_sandwich = bool, amount_of_ketchup_packets = int ):
        self.money = money
        self.items_in_cart = items_in_cart
        self.amount_added_up = amount_added_up
        self.index = index
        self.has_purchased_fries = has_purchased_fries
        self.has_purchased_beverage = has_purchased_beverage
        self.has_purchased_sandwich = has_purchased_sandwich
        self.amount_of_ketchup_packets = amount_of_ketchup_packets

consumer = Consumer(money=100, items_in_cart=[], amount_added_up=0, index=0, has_purchased_fries=False, has_purchased_beverage=False,has_purchased_sandwich=False, amount_of_ketchup_packets=0)

# List and dictionary for items
items_in_cart = []
items_bought = {}
items_available = {"Chicken": 5.25, "Beef": 6.25, "Tofu": 5.75, "Small Beverage": 1.00, "Medium Beverage": 1.75, "Large Beverage": 2.25, "Small Fries": 1.00, "Medium Fries": 1.50, "Large Fries": 2.00}
large_fries_price = items_available["Large Fries"]
large_fries_price_int = int(large_fries_price)
# This is where the consumer will start at
def start_menu():
    clear_screen()

    print("---------------------------------")
    print("Welcome to the Shop Program!")
    print("============================")
    print(f"Current amount of money: {consumer.money}")
    print("[1] Check out available items")
    print("[2] Browse and Buy Items")
    print("[3] View your current items")
    print("[4] Leave the Store")
    match input("Pick your option dear consumer: "):
        case '1':
            available_items()
        case '2':
            browse_items()
        case '3':
            current_items()
        case '4':
            clear_screen()
            input("We hope you enjoyed your Shopping Experience!")
            sys.exit()
        case _:
            input("Invalid option")
            start_menu()
            
def browse_items():
    if consumer.money <= 13.00:
        input("You do not have enough money to shop")
        clear_screen()
        start_menu()
    
    input("Happy Shopping!")

    clear_screen()

    for key, value in items_available.items():
        clear_screen()

        print(f"Item: {key}\nCost: {value}\n===========================\n")
        match input("Would you like to buy this?: [type 'Buy' to Buy!, type 'Skip' to skip!]: ").capitalize():
            case 'Buy':
                consumer.index += 1
                if key == "Small Fries":
                    user_wants_mega_fries = input("Do you want to mega_size your fries? [type 'Yes' to Buy!, enter anything to not buy!]: ")
                    if user_wants_mega_fries.capitalize() == 'Yes':
                        consumer.money -= large_fries_price
                        consumer.amount_added_up += large_fries_price
                        print(f"Current amount of money: {consumer.money}")
                        print(f"Current total cost: {consumer.amount_added_up}")
                        input(f"You have bought Mega sized small frices for the price of: {large_fries_price_int}")
                        input()
                        items_bought[key] = value
                        consumer.money -= value
                        consumer.amount_added_up += value
                        print(f"Current amount of money: {consumer.money}")
                        print(f"Current total cost: {consumer.amount_added_up}")
                else:
                    items_bought[key] = value
                    consumer.money -= value
                    consumer.amount_added_up += value
                    print(f"Current amount of money: {consumer.money}")
                    print(f"Current total cost: {consumer.amount_added_up}")

                    input(f"You have bought {key}.")

                if key == ["Chicken", "Beef", "Tofu"]:
                    consumer.has_purchased_sandwich = True
                if key == ["Small Fries", "Medium Fries", "Large Fries"]:
                    consumer.has_purchased_fries = True
                if key == ["Small Beverage", "Medium Beverage", "Large Fries"]:
                    consumer.has_purchased_beverage = True

            case 'Skip':
                consumer.index += 1
                print(f"Current amount of money: {consumer.money}")
                print(f"Current total cost: {consumer.amount_added_up}")
                input("You have skipped over this item.")
            case _:
                input("Invalid option, decision skipped by default")

    consumer.amount_of_ketchup_packets = int(input("How many ketchup packets would you like it cost .25 cents per packet [Enter a '#']: "))
    ketchup_cost = consumer.amount_of_ketchup_packets * 0.25
    consumer.money -= float(ketchup_cost)
    consumer.amount_added_up += float(ketchup_cost)

    if  consumer.has_purchased_beverage:
        print("You have purchased Beverage")
    elif consumer.has_purchased_fries:
        print("You have purchased Fries")
    elif consumer.has_purchased_sandwich:
        print("you have purchased a Sandwich")
    else:
        input("You can get a combo")
        print(f"The amount of ketchup packets: {consumer.amount_of_ketchup_packets} and the cost {ketchup_cost}")
        consumer.money += 1
        consumer.amount_added_up -= 1

        print(f"Current amount of money: {consumer.money}")
        print(f"Current total cost: {consumer.amount_added_up}")
    input("We hope you enjoyed your Shopping Experience!")
    start_menu()
      
def current_items():
    clear_screen()
    print("Here are all your items you have bought along with the prices attached to said items.")
    
    if items_bought:
        for key, value in items_bought.items():
            print(f"Item: {key}\nCost: {value:}\n**************************\n")
        print(f"Amount of ketchup packets: {consumer.amount_of_ketchup_packets}" )
        input("Type 'ENTER' when you are finished surveying your items")

    else:
        input("You have no items to survey. Press ENTER to return to the main menu.")
    
    start_menu()
    
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def available_items():
    clear_screen()
    print(items_available)
    input("Press 'enter' to return to main menu")
    start_menu()
            
start_menu()

