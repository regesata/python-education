import time


# this section gets time in sec from beginning of the  epoch
t = time.time()
print(t)
# convert in string
print(time.ctime(t))
# custom converting
strf = "%Y, %B, %d, %A "
print(time.strftime(strf, time.localtime()))
strf = "%x, %H:%M"
# using UTC time
print(time.strftime(strf, time.gmtime()))


import datetime

# creating datatime objects
dt = datetime.date(year=1990, month=11, day=4)
print(dt)
time_d = datetime.time(hour=12, minute=9, second=33)
print(time_d)
date_time = datetime.datetime(year=2010, month=11, day=10, hour=12, minute=25, second=22)
print(date_time)

# getting current date and time
cur_date = datetime.date.today()
print(cur_date)
cur_date_time = datetime.datetime.now()
print(cur_date_time)
cur_time = datetime.time(cur_date_time.hour, cur_date_time.minute, cur_date_time.second)
print(cur_time)


# how old are you
DAY_OF_B = datetime.date(year=1987, month=10, day=30)
countdown = DAY_OF_B - datetime.date.today()
print(f"You are{countdown.days//365} years old")


import os

print(f"os name: {os.name}")
print(f"current user name: {os.getlogin()}")
# we change current dir, create folder and remove this folder
os.chdir("res")
os.mkdir("temp")
os.rmdir("temp")

import sys

# get args from command line;
a = sys.argv
print(f"Hello {a[1]}")

os_name = sys.platform
print(os_name)
print(sys.version_info)
