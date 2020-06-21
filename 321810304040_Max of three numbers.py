# Write a Python function to find the Max of three numbers


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a==b==c:
    print("All are equal..No Maximum number")
if (a>b and a>c):
    print("Maximum number is",a)
elif (b>c and b>a):
    print("Maximum number is",b)
else:
    print("Maximum number is",c)