#if3

print("You died!")
question = input("Pay $5 to play again? ")

if question == "Yes" or question == "yes" or question == "y":
    print("Good Luck")
elif question == "No" or question == "no" or question =="n":
    print("Good-Bye")
else:
    print("Type something else than " + str(question))
