height = eval(input("Enter your height in feets :"))
weight = eval(input("Enter your weight in kg :"))
x = round(weight / (height * height) , 2)
print("Mass of your in index is = " , x)