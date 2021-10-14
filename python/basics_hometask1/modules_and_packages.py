import re

# Your code goes here
func_list = [st for st in dir(re) if "find" in st]
func_list.sort()
print(func_list)

