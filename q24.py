x=[]
for y in range(1500, 2701):
    if (y%7==0) and (y%5==0):
        x.append(str(y))
print (','.join(x))