# Area Calculator - ipo8.py

import math

Pi = math.pi
print(Pi)

radius = int(input("What size would you like to set the radius of your circle? (centimeters) "))
print("The radius of your circle is " + str(radius) + "cm.") 

print("The formula to find the area of your circle is the following: A = Pi * diameter")

area = Pi * (radius**2)
print("The area of your circle is " + str(area) + "cm.")
