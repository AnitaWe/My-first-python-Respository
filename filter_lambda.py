
#Use filter and lambda to filter out all odd and even numbers in two different list, and print out the numbers
#Use random to generate a n number of numbers and use sort method

import random

numbers = [random.randrange(1,10000) for i in range(80)]
numbers.sort()

#Filter out only the even number in the list
even_numbers = list(filter(lambda x : (x%2 == 0),numbers))

print("All the even numbers in the list:\n", even_numbers)


#Filter out only the od number in a list
odd_numbers = list(filter(lambda x : (x%2 != 0),numbers))
print("All the odd numbers in the list: \n", odd_numbers)