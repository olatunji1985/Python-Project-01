weight = float(input("Enter your weight: "))
unit = input("Kg or lbs? ")

if unit == 'k':
    converted = weight / 0.45
    print("weight in lbs: " + str(converted))

elif unit == 'l':
    converted = weight * 0.45
    print("weight in kg: "+ str(converted))