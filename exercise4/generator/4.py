m,k=map(int,input().split())
def square(n,b):
    for i in range(n,b+1):
        yield i**2

for x in square(m,k):
    print(x)
