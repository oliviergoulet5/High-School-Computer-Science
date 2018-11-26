import random


# VARIABLES

name = ""
name = str(input("What's your name? "))

# for item in table:
goodbyeList = ["bye", "goodbye", "cya"]
helloList = ["hi", "hello", "hey", "hola"]

# FUNCTION

while True:
    question = str(input("Ask me a question: "))

    #Change Name
    if "change" in question.lower() and "name" in question.lower():
        newname = str(input("What would you like me to call you? "))
        print("Hello, " + newname)
        name = newname

    #Funny Joke
    if "joke" in question.lower() or "funny" in question.lower():
        joke = input("Knock Knock. ")
        joke2= input("Boo ")
        if "who" in joke2.lower():
            print("LOL")

    #Response to spam
    if "a" in question.lower() and "w" in question.lower() and "c" in question.lower() and "q" in question.lower() and "f" in question.lower() and len(question) > 12:
        print("STOP DOING THAT")

    #SPAM

    if "a" in question.lower() and "w" in question.lower() and "c" in question.lower() and "q" in question.lower() and "f" in question.lower() and len(question) > 24:
            x = 0
            
            while x < 25:
                x = x + 1
                print("STOP SPAMMING")
                if x > 25:
                    x = x + 1
                    print("fsbsdbgfadibfsuibfsduiabfasduibfsduibfasduibfasduif")
                    print("fsdnfnasbfbgfbgusdfbgsdfuibgsdfuibgsdfuibgsdfuibgsdfuibgsdfuibgfsdui")
                    print("bnvndnfabnebfbasudbfubeubrgbwqfquwbfqwibfqwibfqwpbfqwibfqwuibfwuqbfqwubfwuiqbfqw")
                    print("cvnxcvuibv xcuibvubfvufdbvsdfuvibsdfuibvdfuibweuewburqweuibr rb weubrweuibr wuebrweurbqweuibrweuibfufbsdu")
