def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current

fib = fibonacci()
c = 0
while c < 21:
    print(next(fib))
    c += 1
