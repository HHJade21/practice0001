
##함수 선언 부분##
def screenLeftClick(x, y) ;
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.togo(x, y)

def screenRiightClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)


##변수 선언 부분##
pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0


##메인 코드 부분##
