#Ask a user and ask for a number and tell if it's a odd or even number


def main():
    x = int(input("Write a number to see if it's odd or even? "))
    print(x , " is an even number" if is_even(x) else " is an odd number")


def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()
