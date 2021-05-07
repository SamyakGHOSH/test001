import sys

try:       
    x = float(input("x = "))
    y = float(input("y = "))
except ValueError:
    print(f"Invalid dumbass put a number")
    sys.exit(1)
try:
    result=x/y
except ZeroDivisionError :
    print(f"Error. Number cannot be divided by Zero")
    sys.exit(1)


print(f"{x} / {y} = {result}")
