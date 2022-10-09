x = eval(input("Enter the first number :"))
y = eval(input("Enter the second number :"))
c = x * y
for i in range(1,c+1):
 if x != 0 or y != 0:
  print("THE LCM IS = ", i)
else:
    print("Ther is no more LCM")
