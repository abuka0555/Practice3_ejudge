nums = [1, 2, 3, 4, 5]

mapped = list(map(lambda x: x * 2, nums))

filtered = list(filter(lambda x: x % 2 == 0, mapped))

print(mapped)
print(filtered)