import turtle
import random
import math

##전역 변수 선언 부분##
angle, distance = 0, 0

##메인 코드 부분##

turtle.title('거북이 서로 만나게 하기')
turtle.setup(width = 350, height = 350)
turtle.screensize(300, 300)

turtle1 = turtle.Turtle('turtle'); turtle1.color('red'); turtle1.penup(); turtle1.goto(-100, -100); turtle1.speed(15)
turtle2 = turtle.Turtle('turtle'); turtle2.color('green'); turtle2.penup(); turtle2.goto(0, 0); turtle2.speed(15)
turtle3 = turtle.Turtle('turtle'); turtle3.color('blue'); turtle3.penup(); turtle3.goto(100, 100); turtle3.speed(15)



while True :
    angle = random.randrange(0, 360)
    distance = random.randrange(30)
    turtle1.right(angle); turtle1.forward(distance)
    angle = random.randrange(0, 360)
    distance = random.randrange(30)
    turtle2.right(angle); turtle2.forward(distance)
    angle = random.randrange(0, 360)
    distance = random.randrange(30)
    turtle3.right(angle); turtle3.forward(distance)

    if math.sqrt(((turtle1.xcor()-turtle2.xcor())*(turtle1.xcor()-turtle2.xcor()))+((turtle1.ycor()-turtle2.ycor())*(turtle1.ycor()-turtle2.ycor()))) <= 20 or \
       math.sqrt(((turtle1.xcor()-turtle3.xcor())*(turtle1.xcor()-turtle3.xcor()))+((turtle1.ycor()-turtle3.ycor())*(turtle1.ycor()-turtle3.ycor()))) <= 20 or \
       math.sqrt(((turtle2.xcor()-turtle3.xcor())*(turtle2.xcor()-turtle3.xcor()))+((turtle2.ycor()-turtle3.ycor())*(turtle2.ycor()-turtle3.ycor()))) <= 20 :
        turtle1.turtlesize(3); turtle2.turtlesize(3); turtle3.turtlesize(3)
        break
    

turtle.done
