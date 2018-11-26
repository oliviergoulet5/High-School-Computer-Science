#if2

number = int(input("Enter a number: "))
secnumber = int(input("Enter a second number: "))

if number == secnumber:
    print(str(number) + " is equal to " + str(secnumber))
elif number > secnumber:
    print(str(number) + " is larger than " + str(secnumber))

elif number < secnumber:
    print(str(secnumber) + " is larger than " + str(number))

