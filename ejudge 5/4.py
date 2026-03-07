import re
s=input()
digt=re.findall(r"\d",s)
print(*digt)