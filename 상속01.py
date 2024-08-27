#부모 클래스 
class Person(object):
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
        self.phoneNumber))

#자식 클래스 
class Student(Person):
    #재정의(override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #재정의
    def printInfo(self):
        print("Info(이름:{0}, 전화번호: {1})".format(self.name, 
        self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, 
        self.studentID))
        
#인스턴스 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터학과", "24111")
p.printInfo()
s.printInfo()



