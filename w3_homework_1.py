import random


##전역 변수 선언 부분##
dicecount, straight = 0, 0
dice1, dice2, dice3, dice4, dice5, dice6 = 0, 0, 0, 0, 0, 0
endnum = 0
diceresult = []

##메인 코드 부분##
##2021041041 소프트웨어학과 홍은성##
while True :
    diceresult = []
    for i in range(0, 6, 1):
        diceresult.append(random.randint(1,6))
    dicecount += 1
    dice1 = diceresult.count(1)
    dice2 = diceresult.count(2)
    dice3 = diceresult.count(3)
    dice4 = diceresult.count(4)
    dice5 = diceresult.count(5)
    dice6 = diceresult.count(6)
    if dice1 == 6 :
        endnum = 1
        break
    elif dice2 == 6 :
        endnum = 2
        break
    elif dice3 == 6 :
        endnum = 3
        break
    elif dice4 == 6 :
        endnum = 4
        break
    elif dice5 == 6 :
        endnum = 5
        break
    elif dice6 == 6 :
        endnum = 6
        break
        

        
    if 1 in diceresult :
        if 2 in diceresult :
            if 3 in diceresult :
                if 4 in diceresult :
                    if 5 in diceresult :
                        if 6 in diceresult :
                            straight += 1

print("6개 주사위 모두 동일한 숫자가 나옴 --> %d %d %d %d %d %d" % (endnum, endnum, endnum, endnum, endnum, endnum))
print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 --> %d" % dicecount)
print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 --> %d" % straight)
