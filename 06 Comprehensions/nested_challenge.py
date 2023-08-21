# In an early video, we used a for loop to print the times tables, for values from 2 to 13.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.
 
print('Multiplication Tables')
# for i in range(2,14):
#     for j in range(1,11):
#         print("{:3} x {:3} = {:3}".format(i,j,i*j))

for i, j in [(i,j) for i in range(2,14) for j in range(1,11)]:
    print(f"{i:3} x {j:3} = {i*j:3}")