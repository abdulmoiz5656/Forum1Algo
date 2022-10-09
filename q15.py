x = eval(input("Enter the number :"))
y = eval(input("Enter the number :"))
z = eval(input("Enter the number :"))
sum = x + y + z
if x == y or y == z or z == x:
    print("The sum of numbers is = 0")
else:
    print("The sum of three number is =" , sum)