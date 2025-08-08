# Add function
def add(a, b):
    print("Answer is:", a + b)

# Subtract function
def subtract(a, b):
    print("Answer is:", a - b)

# Multiply function
def multiply(a, b):
    print("Answer is:", a * b)

# Divide function
def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Answer is:", a / b)

# Ask the user what they want to do
print("What do you want to do???")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter 1, 2, 3, or 4: ")

# Take numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Call the correct function
if choice =="1":
    add(a, b)
elif choice =="2":
    subtract(a, b)
elif choice =="3":
    multiply(a, b)
elif choice =="4":
    divide(a, b)
else:
    print("Wrong choice!")

