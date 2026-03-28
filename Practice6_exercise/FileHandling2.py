with open("text.txt","a") as f:
    f.write("\nI am 18")
with open("text.txt","r") as f:
    print(f.read())
f.close()