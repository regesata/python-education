# regular import
import math
print(math.pow(9, .5))


# import one object from library
from time import time as t
print(t())


# package import
import my_package
my_package.sub_package2
import my_package.sub_package1.func_in_subpckg1 as f
f.my_func()


# resources import
from importlib import resources
with resources.open_text("res", "my_text.txt") as tx:
    file_text = tx.readlines()
    print("".join(file_text))


# dynamic import
from importlib import import_module as im
modules = "os", "sys", "random"
for module_name in modules:
    module = im(module_name)
    print(module.__name__,":", sep="", end=" ")
    arrt_list = [it for it in module.__dict__.keys() if not it.startswith("_")]
    print(" ".join(arrt_list))

