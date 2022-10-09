x = eval(input("Enter your height :"))
f = eval(input("Feets :"))
inch = eval(input("inches :"))
inch += f * 12
cm = round(inch * 2.54 , 1)
print("Your height in centimeters =" , cm)