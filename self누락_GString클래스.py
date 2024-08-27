#전역변수 초기화 
strName = "Not Class Member"

class DemoString:
    #약간 관용적인 표현 
    def __init__(self):
        #인스턴스 멤버 변수 초기화 
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #버그 발생(파이썬은 명확한 것이 좋다!) 
        print(self.strName)

#인스턴스 생성 
d = DemoString()
d.set("First Message")
d.print()
