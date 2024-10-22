class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins:")
        quarters = int(input("How many quarters?: "))  
        dimes = int(input("How many dimes?: "))        
        nickels = int(input("How many nickels?: "))    
        pennies = int(input("How many pennies?: "))   
        
       
        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        print(f"Total inserted: ${total:.2f}")
        return total

    def transaction_result(self, coins, cost):
        """Returns True when payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Transaction successful! Your change is: ${change:.2f}")
            return True
        else:
            print(f"Sorry, not enough money. ${cost - coins:.2f} is still needed.")
            return False

