from sys import stdin
input = stdin.readline

l = [int(input()) for _ in range(9)]
print(max(l))
print(l.index(max(l)))