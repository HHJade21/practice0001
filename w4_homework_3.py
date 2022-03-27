import turtle
import random

##전역 변수 선언 부분##
myt, tX, tY, tcolor, tsize, tshape, tsum = [None] * 7
turtleList = []

##메인 코드 부분##
if __name__ == "__main__" :
    turtle.title('거북이 리스트 정렬해서 선 그리기')
    turtle.setup(width = 450, height = 350)
    turtle.screensize(450, 350)

    for i in range(0, 5, 1) :
        myt = turtle.Turtle('turtle')
        tsize = random.randrange(10, 100)/10
        tX = random.randrange(-250, 250)
        tY = random.randrange(-200, 200)       
        tSum = tX + tY
        
        r = random.random()
        g = random.random()
        b = random.random()

        turtleList.append([myt, tsize, tX, tY, tsum, r, g, b])

    sortedList = sorted(turtleList, key = lambda turtles : turtles[1], reverse = True)

    for index, tList in enumerate(sortedList[0:]):
        myt = tList[0]
        myt.color((tList[5], tList[6], tList[7]))
        myt.pencolor((tList[5], tList[6], tList[7]))
        myt.turtlesize(tList[1])
        myt.penup()
        if index == 0:
            myt.goto(tList[2], tList[3])
            continue
        myt.goto(sortedList[index-1][2], sortedList[index-1][3])
 
        myt.pendown()
        myt.goto(tList[2], tList[3])

turtle.done()
