even = [2,4,6,8]
odd = [1,3,5,7,9]

even.extend(odd)    # Extend method appends another list to the callee list
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)