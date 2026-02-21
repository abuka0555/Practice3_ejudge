def isUsual(num):
    if num <= 0:
        return False

    for p in (2, 3, 5):
        while num % p == 0:
            num //= p

    return num == True

n = int(input().strip())

if isUsual(n):
    print("Yes")
else:
    print("No")
