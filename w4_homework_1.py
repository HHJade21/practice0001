import random

##전역 변수 선언 부분##
data = []
tempdata = 0
i, j, k = 0, 0, 0

##메인 코드 부분##
#2021041041 소프트웨어학과 홍은성#
if __name__ == "__main__" :
    for i in range(0, 10, 1) :
        tempdata = hex(random.randrange(0x1000, 0xFFFF))
        data.append(tempdata)
        
    print("정렬 전 데이터 : ", end = " ")
    [print(num, end = " ") for num in data]
    for j in range(0, 10, 1) :
        for k in range(j+1, 10, 1) :
            if (data[j] > data[k]) :
                temp = data[j]
                data[j] = data[k]
                data[k] = temp

    print("\n정렬 후  데이터 : ", end = " ")
    [print(num, end = " ") for num in data]
