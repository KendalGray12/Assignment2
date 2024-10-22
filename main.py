import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

# Create instances of SandwichMaker and Cashier classes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    
    print("Welcome to the Ham Sandwich Maker!")
    print("Our menu: ")
    print("1. Ham Sandwich - $5.00")
    
    
    sandwich_choice = "ham_sandwich"
    
   
    if sandwich_maker_instance.check_resources(recipes[sandwich_choice]):
        print("The sandwich can be made!")
        
       
        cost = 5.00 
        total_inserted = cashier_instance.process_coins()
        
        
        if cashier_instance.transaction_result(total_inserted, cost):
          
            sandwich_size = int(input("How many sandwiches would you like (1x, 2x, etc.)? "))
            sandwich_maker_instance.make_sandwich(sandwich_size, recipes[sandwich_choice])
        else:
            print("Transaction failed, please try again.")
    else:
        print("Sorry, we don't have enough ingredients to make your sandwich.")

if __name__ == "__main__":
    main()

