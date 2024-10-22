class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, required_amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < required_amount:
                print(f"Sorry, not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Makes a sandwich if resources are sufficient, deducts resources based on sandwich size."""
        scaled_ingredients = {ingredient: amount * sandwich_size for ingredient, amount in order_ingredients.items()}
        
        
        if self.check_resources(scaled_ingredients):
            for ingredient, amount in scaled_ingredients.items():
                self.machine_resources[ingredient] -= amount
            print(f"Here is your {sandwich_size}x sandwich!")
        else:
            print("Could not make sandwich due to insufficient resources.")


