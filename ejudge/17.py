x=int(input())
contacts={}
for i in range(x):
    number=input()
    if number in contacts:
        contacts[number]+=1
    else:        contacts[number]=1
cnt=0
for key in contacts:
    if contacts[key]==3:
        cnt+=1
print(cnt)