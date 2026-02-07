import math
x=int(input())
nums=list(map(int,input().split()))
for i in range(len(nums)):
    nums[i]=int(math.pow(nums[i],2))
print(*nums)