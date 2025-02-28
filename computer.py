from typing import Dict, Union, Optional
class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # Get attributes:
    '''Pseudocode:
1. Do the attributes for init (self, description, processor_type, 
    hard_drive_capacity, memory, operating_system, year_made, price):
2. Initialize the init self.whatever = whatever
3. Do the attributes for update_price (self, inventory, item_id: int, new_price: int)
4. Do the attributes for refurbish (self, inventory, item_id: int, new_os: Optional[str] = None)


'''
    def __init__(self, description, processor_type, 
    hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

       

    # What methods will you need?
     # First, let's make a computer

    ''' def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    } '''


#Why does the item_id work if it's not defined in this file? 


    def update_price(self, inventory, item_id: int, new_price: int):
        if item_id in self.inventory:
             self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
                
    def refurbish(self, inventory, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")