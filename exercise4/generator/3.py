m=int(input())
if m<=1:
    print(0)
else:
    def num(n):
        for i in range(n+1):
            if i%3==0 and i%4==0:
                yield i

    for x in num(m):
        print(x,end=" ")