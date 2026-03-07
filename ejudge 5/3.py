import re
s=input()
p=input()
cnt=re.findall(p,s)
print(cnt.count(p))