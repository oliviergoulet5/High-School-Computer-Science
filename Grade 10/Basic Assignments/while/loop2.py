#loop2

x = 1
answer = True

while answer == True:
    x = x * 2
    print(x)
    question = input("Would you like to keep going?")

    if "no" in question.lower() or "na" in question.lower() or "ne" in question.lower() or "st" in question.lower(): # no. nah, never, stop
        print("Ok I'll stop!")
        answer = False
        
    else:
        print("I'll keep going")
        
    
