import re

s = input()
if re.search("cat",s) or re.search("dog",s):
    print("Yes")
else:
    print("No")