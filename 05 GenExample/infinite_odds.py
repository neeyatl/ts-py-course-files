def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2

odds = odd_numbers()
c = 0
while c < 100:
    print(next(odds))
    c += 1
