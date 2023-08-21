numbers = [13, 22, 44, 9]

for num in numbers:
    if num % 7 == 0:
        print("Numbers divisible by seven not allowed")
        break
else: print("All numbers aren't seven's multiples") # Executes only when the loop completely executes
# If the loop break out, the else block won't be executed
