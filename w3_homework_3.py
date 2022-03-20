

##전역 변수 선언##
i, k, num = 0, 0, 0
numstr, output = "", ""

##메인 코드 부분##

numstr = input("숫자를 여러 개 입력하세요 : ")

for i in range(0, len(numstr), 1) :
    output = ""
    for k in range(0, int(numstr[i]), 1) :
        output += "\u2665"
    print("%s" % output)
