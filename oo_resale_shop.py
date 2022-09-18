from typing import Dict, Union, Optional
class ResaleShop:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   
# Added attributes here (why is the self attribute a different color?)
    def __init__(self, inventory):
        #Nested dictionary: first dictionary is an integer 
        # which is mapped onto another dictionary with a string which is mapped onto a union?? :/
        inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}
        def buy(self, computer: Dict[str, Union[str, int, bool]]):
            global itemID
            itemID += 1 # increment itemID
            self.inventory[itemID] = computer
            return itemID
        def print_inventory(self):
            # If the inventory is not empty
            if inventory:
                # For each item
                for item_id in inventory:
                    # Print its details
                    print(f'Item ID: {item_id} : {inventory[item_id]}')
            else:
                print("No inventory to display.")

        def sell(item_id: int):
            if item_id in inventory:
                del inventory[item_id]
                print("Item", item_id, "sold!")
            else: 
                print("Item", item_id, "not found. Please select another item to sell.")
                
        sell(1)

        


        
    # What methods will you need?

