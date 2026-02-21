numbers={"ONE":"1","TWO":"2","THR":"3","FOU":"4","FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9"}
triplets={"1":"ONE","2":"TWO","3":"THR","4":"FOU","5":"FIV","6":"SIX","7":"SEV","8":"EIG","9":"NIN"}
n = input()
if "+" in n:
    operator="+"
elif "-" in n:
    operator="-"
elif "*" in n:
    operator="*"
a,b=n.split(operator)
def to_num(c):
    num=""
    for i in range(0,len(c),3):
        num+=numbers[c[i:i+3]]
    return num
    


num1=to_num(a)
num2=to_num(b)

if operator=="+":
     res=int(num1)+int(num2)
elif operator=="-":
     res=int(num1)-int(num2)
elif operator=="*":
     res=int(num1)*int(num2)

res = str(res)

for digit in res:
    print(triplets[digit], end="")
    


