# Knapsack problem 

# Given a set of items, each with a weight and a value, 
# determine which items to include in the collection 
# so that the total weight is less than or equal to a given limit 
# and the total value is as large as possible.

class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        
def fractional_knapsack(items, capacity):
    """
    returns (maxvalue, fractions)
    maxvalue => the maximum value of selected item within capacity
    fractions => dictionary showing selected items and serving fraction
    
    input (items, capacity)
    items => choices
    capacity => knapsack capacity ( sort of like the upperbound )
    """
    
    # sort the items by value/weight ratio, highest on top
    # reason=> as you will loop through the item list, you want the best ones to eat first
    
    items.sort(key= lambda item: item.value/item.weight, reverse = True)
    
    max_value = 0
    fractional_amount = {}
    
    for item in items:
        
        # imagine you can eat 100 g per meal
        # to maximize the satisfaction, you wanna eat as much of your fav food as you can
        # (Health comes later) from the whole buffet
        
        if(item.weight <= capacity):
            fractional_amount[item] = 1
            max_value += item.value
            capacity -= item.weight
        else :
            # imagine you only have little room one full cake (desert)
            # you will cut the cake down to the amount you still fit
            fraction_to_add = capacity / item.weight
            fractional_amount[item] = fraction_to_add
            max_value += item.value * fraction_to_add
            # break because when this runs, it's most likely that this will be the last of the meal
            break
        
    return max_value, fractional_amount
        
items = [
    Item('Peanut', 90, 30),
    Item('Sunflower Seed', 45, 30),
    Item('Coconut Water', 140, 80),
    Item('Macademin Seed', 90, 20)
]

capacity = 100

max_value, fractions = fractional_knapsack(items, capacity)

print('The max value of item that can be taken within capacity:', capacity)

for item in fractions:
    print('item:', str(item.name))
    print('amount:', str(fractions[item]))