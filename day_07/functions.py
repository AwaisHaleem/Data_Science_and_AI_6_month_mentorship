# fn is a block of code that runs when it is called

# *declaration/defination of function
def hello():
    print("Hello World")


# * calling the fn
hello()


# * making functions with parameters
def greeting(name):
    print("Hello ", name)


# calling function with arguments
greeting("Ali")

# *function with default values


def greeting(name="Mr."):
    print("Hello ", name)


# calling fn with out argument
greeting()      # prints Hello Mr.
# calling greeting with name
greeting("Hamza")       # prints Hello Hamza


# * Function with return value
def square(x: int) -> int:
    return x**2


print(square(4))

squareed = square(2)   # will return 16
print(squareed)

# * defining function with named arguments


def greeting(name: str = "Mr") -> str:
    return ("Hello", name)


print(greeting("Ali"))

# * Recursion
# when a fucntion call itsel

# factorial function with recrusion


def factorial(number: int) -> int:

    if number == 1:       # break limit
        return 1
    return factorial(number-1)*number


print(factorial(5))

# * lambda function like arrow function in js


# add_10 = lambda a: a+10


# print(add_10(10))
