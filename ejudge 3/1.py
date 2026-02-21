number=input()
def checking_even(number):
    bool=True
    for i in number:
        if int(i)%2!=0:
            bool=False
            break
    return bool
if checking_even(number):
    print("Valid")
else:
    print("Not valid")
   