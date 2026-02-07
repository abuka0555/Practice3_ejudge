n = int(input())
nums = list(map(int, input().split()))

count = {}
for x in nums:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

max_freq = 0
answer = 0
for key in count:
    if count[key] > max_freq:
        max_freq = count[key]
        answer = key
    elif count[key] == max_freq and key < answer:
        answer = key

print(answer)
