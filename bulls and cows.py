secret=int(input("enter secret number"))
guess=int(input("enter guess number"))
secretList=[d for d in str(secret)]
guessList=[d for d in str(guess)]
print(secretList)
print(guessList)
x=0
y=0
for i,d in enumerate(secretList):
    if d in guessList:
        if secretList[i]==guessList[i]:
            x=x+1
        else:
            y=y+1
ans=str(x)+"A"+str(y)+"B"
print(ans)
