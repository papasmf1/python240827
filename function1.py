# function1.py 
#1)함수 정의
def setValue(newValue):
    #지역변수 초기화
    x = newValue
    print("지역변수:", x)

#2)호출
retValue = setValue(5)
print(retValue)

#함수 정의
def swap(x,y):
    return y,x 

#호출
retValue = swap(3,4)
print(retValue)


