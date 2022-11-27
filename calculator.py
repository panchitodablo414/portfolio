x = int(input("Enter first number:"))
op = input("Enter operator:")
y = int(input("enter second number:"))



if op == "+":
    print (x + y)
elif op == "-":
    print (x - y)
elif op == "/":
    print(x / y)
elif op== "*":
    print (x *y)
elif op == "%":
    print(x%y)
else:
    print("Enter valid operator")
