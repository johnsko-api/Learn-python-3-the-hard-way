def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print (f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

puzzle = add(age, subtract(height,multiply(weight, divide(iq,2))))

# divide iq by 2 so 25
# multiply weight * 25 = 4500
# subtract height - 4500 = -4426
# add age + -4422 = -4391

print(puzzle)
