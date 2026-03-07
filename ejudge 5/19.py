import re
s=input()
pattern=re.compile(r"\w+")
result=pattern.findall(s)
print(len(result))