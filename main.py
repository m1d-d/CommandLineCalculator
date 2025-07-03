print("Please insert the first value")
val1 = int(input())
print("Now insert the second value")
val2= int(input())
print("What you want to mean with these values?")
print("Sum, Subtract, Multiply, Divide")
operation = str(input())

if operation == "Sum":
    result = val1 + val2
    print(f"The sum of the values is {result}") 
elif operation == "Subtract":
     result = val1 - val2
     print(f"The subtraction of the values is {result}")
elif operation == "Multiply":
     result = val1 * val2
     print(f"The multiply of the values is {result}")
elif operation == "Divide":
     result = val1 / val2
     print(f"The division of the values is {result}")
else:
     print("Invalid values")