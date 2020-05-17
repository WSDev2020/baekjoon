from sys import stdin

data = [int(x) for x in input().strip().split()]

A = data[0]
B = data[1]
C = data[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
