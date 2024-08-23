# def greet(name="Guest"):

#     print(f"Hello, {name}! Welcome to Python!")

# greet()

# greet("Bob")

# def multiply(x, y):

#     return x * y

# result = multiply(9, 7)

# print(result)


# def check_number(number):
#     if number > 0:
#         return "The number is positive."
#     elif number < 0:
#         return "The number is negative."
#     else:
#        return "The number is zero."
    
# print(check_number(10))   # Output: The number is positive.
# print(check_number(-5))   # Output: The number is negative.
# print(check_number(0))    # Output: The number is zero.


# def greet(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")

# greet("John", "Doe")

# def greet(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")

# greet(last_name="Doe", first_name="John")

# def greet(first_name, last_name="Smith"):
#     print(f"Hello, {first_name} {last_name}!")

# greet("John")         # Uses default last name
# greet("Jane", "Doe")  # Overrides default last name


# def greet(*names):
#     for name in names:
#         print(f"Hello, {name}!")

# greet("John", "Jane", "Doe")

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# fruits.append("orange")

# print(fruits) 

# fruits = ["apple", "banana", "cherry"]
# more_fruits = ["mango", "orange"]
# fruits.extend(more_fruits)
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'mango', 'orange']

fruits = ["apple", "banana", "cherry"]
popped_fruit = fruits.pop(1)
print(fruits)       # Output: ['apple', 'cherry']
print(popped_fruit) # Output: 'banana'



