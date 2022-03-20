import turtle

## 전역 변수 선언 부분##
row, column, turtlemove = 0, 0, 0
guguout = ""

##메인 코드 부분##
#2021041041 소프트웨어학과 홍은성
if __name__ == "__main__" :
    turtle.title('거북 구구단')
    turtle.shape('turtle')
    turtle.speed(2)
    turtle.setup(width = 850, height = 500)
    turtle.screensize (800, 450)
    turtle.penup()
    turtle.goto(-410, 210)
    
    for row in range(2, 10, 1):
        guguout = ""
        for column in range(1, 10, 1) :
            guguout = str("%2d X%2d =%2d  " % (row, column, row*column))
            turtle.goto(-500 + 90 * column, 250 - 40 * row)
            turtle.write(guguout, ('Arial', 12, 'bold'))
        
        

            

    turtle.done()
