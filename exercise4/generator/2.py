m=int(input())
if m<=1:
    print(0)
else:
    def even(n):
        for i in range(n+1):
            if i%2==0:
                yield i

    num=[x for x in even(m)]
    print(",".join(map(str,num)))