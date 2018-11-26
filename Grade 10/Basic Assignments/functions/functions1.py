#functions1

#not sure if the formula's correct

while True:

    answerF = None
    answerC = None
    cORf = input("Do you want to find the Celsius or Fahrenheit? ")

    def celsConvert():
        value = int(input("Enter how many degrees(celsius) here: "))
        answerC = value
        print(str(answerC - 32 / 9 * 5) + "F")

    def fahrConvert():
        value = int(input("Enter how many degrees(fahrenheit) here: "))
        answerF = value
        print(str(answerF + 32 * 9/5) + "C")
        

    if (cORf == "Celsius"):
        fahrConvert()

    elif (cORf == "Fahrenheit"):
        celsConvert()

