names = ["Ali", "Bob", "Eve"]

for i, name in enumerate(names, start=1):
    print(i, name)

names = ["Ali", "Bob"]
scores = [90, 80]

for name, score in zip(names, scores):
    print(name, score)