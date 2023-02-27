import random

START = 1
STOP = 500
how_many = input("insert the amount of numbers: ")
how_many = int(how_many)

# https://www.w3schools.com/python/ref_random_randint.asp
f = open("random.txt", "w")
NL ='\n'
for num in range (0, how_many):
    number = random.randint(START, STOP)
    if(num == how_many-1):
        NL = ''
    f.write(str(number)+NL)
f.close()
f = open("random.txt", "r")
print(f.read())