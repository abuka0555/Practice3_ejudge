n = int(input())
strings = []

for _ in range(n):
    strings.append(input())

first_index = {}

for i in range(n):
    s = strings[i]
    if s not in first_index:
        first_index[s] = i + 1  

for s in sorted(first_index.keys()):
    print(s, first_index[s])
