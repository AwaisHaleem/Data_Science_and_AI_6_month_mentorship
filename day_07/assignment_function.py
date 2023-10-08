# * 10 Functions with def
def square(x: int) -> int:  # 1
    return x**2


def cube(x: int) -> int:  # 2
    return (x**3)


def greeting(name: str) -> str:     # 3
    return f"Hello {name}"


def add_two_two_numbers(x: int, y: int) -> int:  # 4
    return x+y


# add fucntion with infinity number of args
def add(*numbers: int) -> int:  # 5
    result = 0
    for num in numbers:
        result += num
    return result


# function with unlimited kwargs
def map(**kwargs: (str, int)) -> dict:  # 6
    m = {}
    for key, value in kwargs.items():
        m[key] = value
    return m

# * recursion fucntion


def factorial(number: int) -> int:  # 7

    if number == 1:       # break limit
        return 1
    return factorial(number-1)*number

# * lambda functions

# add_10 = lambda a: a+10   #*8

# square = lambda a: a**2   #*9

# square_root = lambda a: a**(1/2)  #*10
