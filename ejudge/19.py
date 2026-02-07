x=int(input())
serials={}
for i in range(x):
    key,value=input().split()
    value=int(value)
    if key in serials:
        serials[key]+=value
    else:        serials[key]=value
for key in sorted(serials.keys()):
    print(key, serials[key])