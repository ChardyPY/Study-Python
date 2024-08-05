print("Welcome to Richard's Calculator!")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")

operation = input()

if operation == "1":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum of the numbers are" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the substraction of the numbers are" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the multiplication of the numbers are" + str(int(num1) * int(num2)))
elif operation =="4":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the division of the numbers are" + str(int(num1) / int(num2)))
else:
    print("give valid operation")