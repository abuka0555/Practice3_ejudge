n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for i in range(q):
    parts = input().split()
    op = parts[0]

    if op == "add":
        x = int(parts[1])
        func = lambda a, x=x: a + x

    elif op == "multiply":
        x = int(parts[1])
        func = lambda a, x=x: a * x

    elif op == "power":
        x = int(parts[1])
        func = lambda a, x=x: a ** x

    elif op == "abs":
        func = lambda a: abs(a)


    arr = list(map(func, arr))

print(*arr)