inum=int(input("Input a number so you know its factorial: "))
fp=1
for i in range(1,inum + 1):
    fp = fp*i
print("The factorial of",inum,"is",fp)