from icecream import ic

# Basic example
a = 5
b = 10
ic(a + b)  # Output: ic| a + b: 15

# Using ic() in functions
def add(x, y):
    result = x + y
    ic(result)  # Output: ic| result: 10
    return result

add(3, 7)

# Debugging inside a loop
for i in range(3):
    ic(i, i**2) # Output:
                # ic| i: 0, i**2: 0
                # ic| i: 1, i**2: 1
                # ic| i: 2, i**2: 4

# Customizing the prefix
ic.configureOutput(prefix='🐍 Debug | ')
ic("Hello, world!")  # Output: 🐍 Debug | "Hello, world!"

# Disabling and enabling ic()
ic.disable()
ic("This will not be printed.")  # No output

ic.enable()
ic("Now it will be printed.")  # Output: ic| "Now it will be printed."

# Using ic() with lambda
square = lambda x: ic(x * x)
square(4)  # Output: ic| x * x: 16
