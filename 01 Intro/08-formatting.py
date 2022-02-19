from cmath import pi


for i in range(1,14):
    print("Number {0:2} squared is {1:3} and it's {2:4} when cubed."
          .format(i, i**2, i**3))
# index:width is the way to format the string to have a predefined width.
# Very important for providing consistent width for maximum readability.

print()

# Follow ':' with a '<' sign to left align the output substring. '^' centers the substring.
for i in range(1,14):
    print("Number {0:2} squared is {1:<4} and it's {2:^4} when cubed."
          .format(i, i**2, i**3))
    
print()

# To set the precision of a float number, follow width with '.' which is then followed by the precision value.
print('PI is approximately {0:.9}'.format(pi))      # Prints a precision of 8
print('PI is approximately {0:.8f}'.format(pi))     # Prints a precision of 8
print('PI is approximately {0:<12.21f}'.format(pi)) # Prints 21 precision with weight 12 and left alignment

print()

# Field numbers are optional. Mandatory to reuse a field multiple times.
for i in range(1,14):
    print("Number {:2} squared is {:<3} and it's {:^4} when cubed."
          .format(i, i**2, i**3))

print()

# f-strings; not supported by lesser versions of python 3; less than 3.4
price = 367.50
print("Joel " + f'bought a pizza for {price} rupees.') # Works like Kotlin or JS special strings syntax-wise

print()

print(f'PI is approximately {22/7:^58.50f}')
