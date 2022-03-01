trace = ''

for i in range(0,10):   # Upto but not including 10
    trace+=str(i)

print(trace)

for i in range(10):     # Start value defaults to 0
    trace+=str(i)

print(trace)

# Have to use a start value when you want to use steps as well
for i in range(0, 10, 2):   # Negative step value to go backwards
    print(i)

print('Multiplication Tables')
for i in range(2,14):
    for j in range(1,11):
        print("{:3} x {:3} = {:3}".format(i,j,i*j))

print('done!')
