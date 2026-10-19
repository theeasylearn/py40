# 0 1 1 2 3 5 8 11 .... 1000
#     p c n
previous = 0
current = 1

print(previous,end=' ')
print(current,end=' ')

while current< 987:
    next = previous + current
    print(next,end=' ')
    previous = current
    current = next

