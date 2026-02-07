x = int(input())
nums = list(map(int, input().split()))

min_val = min(nums)
max_val = max(nums)

for i in range(len(nums)):
    if nums[i] == max_val:
        nums[i] = min_val

print(*nums)
