import re

op = "y"
while op == "y":
    a,b,c  = re.split("[, ]+", input("Enter three numbers separated by spaces: "))

    print("Numbers entered:", a, b, c)
    print("\nSmallest:")

    if a < b:
        if a < c:
            smallest = a
        else:
            smallest = c
    elif b < c:
        smallest = b
    else:
        smallest = c

    print(smallest)

    op = input("Again (y/n)? ")

print("The End.")
