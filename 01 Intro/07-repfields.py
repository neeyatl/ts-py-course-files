age = 22
weight = 78
height = "5'11"
print("My age is {0} years. I weight {1} which is fine for a {2} tall man.".format(age,weight,height))
# Gotta remember that it's '.' format, not ',' as in C or Java printf functions.

print('''\nJan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {1}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}'''.format(28,30,31))   # Recreated a good string replacement fields example