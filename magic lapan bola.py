import random
ans1= ("eh, your laobu raised a siaolang")
ans2= ("try re-rolling again")
ans3= ("No, im afraid you suck ")
ans4= ("Yes correct!")
ans5= ("KYS")
ans6= ("please try again")
ans7= ("The answer is yes")
ans8= ("that is 100% correct")
print ("Welcome to the Magic 8 Ball")
cat= True
while cat== True:
    question= input ("Please ask any question then i shall answer it 4 u ")
    print("shaking")
    choice= random.randint(1,8)
    if choice== 1:
        answer= ans1
    if choice== 2:
        answer=ans2
    if choice== 3:
        answer= ans3
    if choice== 4:
        answer= ans4
    if choice== 5:
        answer= ans5
    if choice== 6:
        answer= ans6
    if choice== 7:
        answer= ans7
    if choice== 8:
        answer= ans8
    print (answer)
    
        
