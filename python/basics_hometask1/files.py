from _functools import reduce
from os import remove
# creating a file and write some data to it
FILE_NAME = "my_file.txt"
with open(FILE_NAME, 'w') as f:
    f.write("Hello,  World!\n")
    st = [str(x) for x in range(21) if x % 2 == 0]
    st = " ".join(st)
    f.write(st)
    f.close()

# open file and read data from it
with open(FILE_NAME) as f:
    temp = f.readline()
    print(temp)
    a = f.read().split()
    a = list(map(int, a))
    summ = reduce((lambda x,y: x+y),a)
    print(summ)
    f.close()
# removing used file
try:
    remove(FILE_NAME)
except FileNotFoundError:
    print("Can`t delete file! File dose not exist")
except IsADirectoryError:
    print("Can`t delete file! File is a directory ")



