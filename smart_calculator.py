print("SMART CALCULATOR")

#ask user two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#ask user to choose operations
print("choose operations: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice=input("choose 1/2/3/4 :")

#logic
if choice == "1":
    print("result = ", num1+num2) 
elif choice == "2":
    print("result = ", num1-num2)
elif choice == "3":
    print("result = ", num1*num2)
elif choice == "4":
    print("result = ", num1/num2)
else:
    print("You have not selected the correct choice")




