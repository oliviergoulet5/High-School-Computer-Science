# Temperature Converter - ipo6.py

# 1 cel = 33.8. The formula is [FAHR = CELS * 1.8 + 32]

cels = float(1)
fahr = float(33.8)

converter = input("How cold is it outside(celsius)? ")
formula = float(converter) * 1.8 + 32
print("I think that's " + str(formula) + " degrees in fahrenheit")

