a = int(input("Insert first number:\n"))
b = int(input("Insert second number:\n"))
equals = 0

action = int(input("What do you want to perform?\n\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n\nNote: Only write a number without a dot.\n"))

if action == 1:
    equals = a + b
elif action == 2:
    equals = a - b
elif action == 3:
    equals = a * b
elif action == 4:
    equals = a / b
else:
    print("Bad option. Try again.")

print(f"Your result is: {equals}")