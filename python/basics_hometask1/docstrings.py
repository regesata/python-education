def my_func():
    """This is docstring of this function"""
    pass


func_tuple = map, abs, print, zip, len, my_func
# getting docstrings from some functions
for f in func_tuple:
    print(f, f.__doc__, end="\n\n")

