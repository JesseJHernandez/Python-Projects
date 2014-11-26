food_prices = {"apple": .65, "dragonfruit": 6.35, "mango": 1.20, "pear": 1.75, "spinach" : 1.13}

food_inventory = {"apple": 3, "dragonfruit": 1, "mango": 0, "pear": 4, "spinach": 5}

shopping_cart = []

shopping_cart = ["apple","mango"]

def total_price (shopping_cart):
#Take list and return price for items in Shopping Card

	cost = 0
	for item in shopping_cart:
		cost = cost + food_prices[item]
	return cost

def inventory (shopping_cart):

	for item in shopping_cart:
		food_inventory[item] -=1

print food_inventory
inventory(shopping_cart)
print food_inventory
#cant be less than 0



#print current inventory, print out of stock
def main():
	price = total_price(shopping_cart)
	print "You have purchased the following items: ",
	for item in shopping_cart:
		print item,
	print "The total cost is %s " % (price)
#main()