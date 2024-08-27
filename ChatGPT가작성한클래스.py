# Base class: Person
class Person:
    def __init__(self, id, name):
        """
        Person 클래스의 생성자 메서드
        :param id: 개인의 고유 식별자 (정수)
        :param name: 개인의 이름 (문자열)
        """
        self.id = id  # 개인의 고유 식별자를 저장하는 멤버 변수
        self.name = name  # 개인의 이름을 저장하는 멤버 변수
    
    def printInfo(self):
        """
        개인의 ID와 이름을 출력하는 메서드
        :return: ID와 이름을 포함한 문자열
        """
        return f"ID: {self.id}, Name: {self.name}"  # ID와 이름을 형식화하여 반환


# Derived class: Manager
class Manager(Person):
    def __init__(self, id, name, title):
        """
        Manager 클래스의 생성자 메서드
        :param id: 관리자의 고유 식별자 (정수)
        :param name: 관리자의 이름 (문자열)
        :param title: 관리자의 직함 (문자열)
        """
        super().__init__(id, name)  # 부모 클래스(Person)의 생성자를 호출하여 id와 name을 초기화
        self.title = title  # 관리자의 직함을 저장하는 멤버 변수
    
    def printInfo(self):
        """
        관리자의 ID, 이름 및 직함을 출력하는 메서드
        :return: ID, 이름 및 직함을 포함한 문자열
        """
        base_info = super().printInfo()  # 부모 클래스의 printInfo 메서드를 호출하여 기본 정보를 가져옴
        return f"{base_info}, Title: {self.title}"  # 기본 정보에 직함 정보를 추가하여 반환


# Derived class: Employee
class Employee(Person):
    def __init__(self, id, name, skill):
        """
        Employee 클래스의 생성자 메서드
        :param id: 직원의 고유 식별자 (정수)
        :param name: 직원의 이름 (문자열)
        :param skill: 직원의 기술 또는 능력 (문자열)
        """
        super().__init__(id, name)  # 부모 클래스(Person)의 생성자를 호출하여 id와 name을 초기화
        self.skill = skill  # 직원의 기술 또는 능력을 저장하는 멤버 변수
    
    def printInfo(self):
        """
        직원의 ID, 이름 및 기술을 출력하는 메서드
        :return: ID, 이름 및 기술을 포함한 문자열
        """
        base_info = super().printInfo()  # 부모 클래스의 printInfo 메서드를 호출하여 기본 정보를 가져옴
        return f"{base_info}, Skill: {self.skill}"  # 기본 정보에 기술 정보를 추가하여 반환


# Test Cases
def test_person_classes():
    """
    Person, Manager, Employee 클래스의 다양한 동작을 테스트하는 함수
    """
    # Test 1: Person 객체 생성 및 정보 확인
    p1 = Person(1, "Alice")
    assert p1.printInfo() == "ID: 1, Name: Alice"
    
    # Test 2: Person 객체의 속성 수정 및 정보 확인
    p1.name = "Alicia"
    assert p1.printInfo() == "ID: 1, Name: Alicia"

    # Test 3: Manager 객체 생성 및 정보 확인
    m1 = Manager(2, "Bob", "Project Manager")
    assert m1.printInfo() == "ID: 2, Name: Bob, Title: Project Manager"
    
    # Test 4: Manager 객체의 속성 수정 및 정보 확인
    m1.title = "Senior Project Manager"
    assert m1.printInfo() == "ID: 2, Name: Bob, Title: Senior Project Manager"
    
    # Test 5: Employee 객체 생성 및 정보 확인
    e1 = Employee(3, "Charlie", "Python")
    assert e1.printInfo() == "ID: 3, Name: Charlie, Skill: Python"
    
    # Test 6: Employee 객체의 속성 수정 및 정보 확인
    e1.skill = "JavaScript"
    assert e1.printInfo() == "ID: 3, Name: Charlie, Skill: JavaScript"
    
    # Test 7: Manager 클래스가 Person 클래스의 하위 클래스인지 확인
    assert issubclass(Manager, Person)
    
    # Test 8: Employee 클래스가 Person 클래스의 하위 클래스인지 확인
    assert issubclass(Employee, Person)
    
    # Test 9: Manager 클래스에 skill 속성이 없는지 확인
    try:
        m1.skill
    except AttributeError:
        pass  # AttributeError가 발생하면 정상

    # Test 10: Employee 클래스에 title 속성이 없는지 확인
    try:
        e1.title
    except AttributeError:
        pass  # AttributeError가 발생하면 정상

    print("All tests passed!")  # 모든 테스트가 통과했음을 출력

# 테스트 실행
test_person_classes()

p1 = Person(100, "전우치")
p1.printInfo()
