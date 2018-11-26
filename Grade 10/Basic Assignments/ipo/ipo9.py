# Pythagorean Formula - ipo9.py

import math

print("All numbers you input will be measured into centimeters!")

side1 = int(input("What long do you want the side1 of your right triangle to be? "))
side2 = int(input("How long do you want the side2 to be? "))

newSide1 = side1 ** 2
newSide2 = side2 ** 2

addSides = newSide1 + newSide2
hypotenuse = math.sqrt(addSides) #Credit: tutorialspoint.com/python/number_sqrt.htm


print("The hypotenuse of your right triangle is " + str(hypotenuse) + "cm.")
