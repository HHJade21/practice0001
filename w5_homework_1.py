

##전역 변수 선언 부분##
i = 0
b = []


##메인 코드 부분##
#2021041041 소프트웨어학과 홍은성#

a = input('문자열을 입력하세요 : ')

i = len(a)


for j in range(i) :
    
    if(a[j].isupper()) :
        b.append(a[j].lower())
    elif(a[j].islower()) :
        b.append(a[j].upper())
    else :
        b.append(a[j])


print("대소문자 변환 결과 -- > ", ''.join(b))
