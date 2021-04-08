# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"call {function.__name__} with {args} and {kwargs}: {function(*args, **kwargs)}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def function_to_log(value, key):
    return f"getting {value} and {key}"


function_to_log("dies und das", "key")