#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
a = input("What is the a value?")
b = input("What is the b value?")
c = input("What is the c value?")

a = float(a)
b = float(b)
c = float(c)
x = (c - b) / a
print(f"The x value is {x}")