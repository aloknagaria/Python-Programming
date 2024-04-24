name = input("Enter the name: ")
weight = int(input("Enter the weight:"))
print(weight)
height = float(input("enter the height in inches:"))
print(height)
BMI = (weight * 703)/(height*height)

print(BMI)
# Alex

if BMI>0:
    if BMI <18.5:
        print(name + " Underweight")
    elif BMI<=24.9:
        print(name + " Normal Weight")
    elif BMI <=29.9:
        print(name + " Over weight")
    else:
        print(name + " Severly mote ho tum")