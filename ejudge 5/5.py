import re
s=input()
if re.search(r"^[a-z].*\d$",s,re.IGNORECASE):
    print("Yes")
else:
    print("No")