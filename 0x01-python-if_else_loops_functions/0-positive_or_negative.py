#!/usr/bin/python3
import random
number = random.randint(-20, 20)
if number > 0:
print("{:d} is positive".format(number))
elif number == 0:
print("{:d} is zero".format(number))
else:
print("{:d} is negative".format(number))
