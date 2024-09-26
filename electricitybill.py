a=float(input("Enter a previous units:"))
b=float(input("Enter a current units:"))
c=a-b
print(c)
if c<=50:
    print("congrats its free!")
elif c>=50 and c<=100:
    print("Your amount is:",c*2.60)
elif c>=101 and c<=200:
    print("Your amount is:",c*3.30)
else:
    print("Invalid")