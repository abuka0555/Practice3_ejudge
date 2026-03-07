def square(n):
    for i in range(n):
        yield i**2
m=int(input())
for x in square(m):
    print(x)