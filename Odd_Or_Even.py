#Ask a user and ask for a number and tell if it's a odd or even number

number = int(input("Write a number to see if it's odd or even? "))

if(number % 2 == 0):
    print(number , " is an even number")
else:
    print(number, " is an odd number")
