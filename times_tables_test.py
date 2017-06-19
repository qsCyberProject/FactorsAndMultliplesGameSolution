# Factors and multliple game random sequence calculator.
# Written by Teymour Aldridge
# Made in python 3, if you are running python 2 this program won't work.
# import the random package
import random
num = random.randint(1,100)
# Set the loop value (used later in the while ... loop)
loop_value = 0
# Variable to store the length of the chain
length_list = 0
# List of used numbers (cant be re-used)
used_numbers = list()
# Python Program to find the factors of a number
# define the list current
current = [1,2,3,4,5]
# define a function to find factors of num
def print_factors():
   # Make variables global
   global current
   global num
   for i in range(1, num + 1):
       if num % i == 0:
           current.append(i)
   if num in current:
       current.remove(num)
# define a function to find multiples of num
def print_multliples():
    # Make variables global
    global current
    global num
    i=1
    # Find multiples
    while i*num < 100:
        # add i*num to the current list
        current.append(i*num)
        # Make sure that the current number is not put in current (list)
        if num in current:
            current.remove(num)
        # Increase i by one
        i=i+1
# Change this line to < (length of chain you want)
while length_list < 59:
    if not current:
        num = random.randint(1,100)
        used_numbers = list()
        length_list = 0
    # clear current
    current = list()
    # Get factors
    print_factors()
    # Find multiples
    print_multliples()
    # ensure that no used numbers are chosen
    current = [x for x in current if x not in used_numbers]
    # make a random number between 0 and the length of current
    # factor=random.randint(0, len(current))
    # Add exception so the program can continue running even when the chain ends
    try:
        #chose a random factor/multliple
        num = random.choice(current)
    except:
        pass
    # Add chosen number to used_numbers
    used_numbers.append(num)
    # Increase length_list by 1
    length_list=length_list+1
print("Found a sequence of " + str(length_list))
print(used_numbers)
