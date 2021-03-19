# varargs Positional Parameter 
# * ist wichtig, Name ist beliebig
def add(*args):
    result = 0
    for n in args:
        result += n

    return result

print(add(2, 4, 2, 3, 6, 7, 5, 4))


# varargs Keyword Parameter 
# ** ist wichtig, Name ist beliebig
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiplay"]

    return n

print(calculate(2, add=2, multiplay=5))