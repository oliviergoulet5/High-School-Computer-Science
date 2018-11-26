unitCost = float(input("Put a price on this gum ball!"))
quantity = int(input("That's a good price! How many gum balls do you want in your machine?"))
#Quantity is set to an Integer because you won't sell half a gum ball.
totalCost = unitCost * quantity

print("This shippment will be priced at $" + str(totalCost) + ".")
