# def decorator_function(original_function):
#     print("Inside decorator function")
#     def wrapper_function(*args, **kwargs):
#         print("Inside wrapper function")
#         return original_function(*args, **kwargs)
#     print("End of decorator function")
#     return wrapper_function

# # @decorator_function
# def simple_function():
#     print("Simple function")

# simple_function = decorator_function(simple_function)
# # decorated_function = decorator_function(simple_function)
# # decorated_function()

# if __name__ == '__main__':
#     simple_function()


def decorator_function(original_function):    
    print("In decorator function")
    def wrapper_function(*args, **kwargs):
        print("In wrapper function")
        return original_function(*args, **kwargs)
    print("End of decorator function")
    return wrapper_function

def display(name, age):
    print(f"display function {name}, {age}")


display = decorator_function(display)
display('tjisana',33)