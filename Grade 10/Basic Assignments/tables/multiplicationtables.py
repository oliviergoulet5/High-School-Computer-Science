question = int(input("Which time table do you want? "))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

for i in numbers:
    answer = i * question
    print(str(i) + " x " + str(question) +  " = " + str(answer))


