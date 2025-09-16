#Displat basic welcome message
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)

# Store some numbers in variables
x = 10
y = 5

# Perform some basic math operations
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

# Print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Ask the user for their name and store the response in the 'name' variable
name = input("What is your name? ")

# Use the 'name' variable to create a personalized greeting
print("Hello, " + name + "!")

# Let's also use a number.
# We'll ask the user for their age, but first we need to convert the text to a number
age_text = input("How old are you? ")
age = int(age_text) # This converts the text 'age_text' into an integer

# Now we can do a calculation with the age
print("In one year, you will be", age + 1, "years old.")
