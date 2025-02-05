# py07_person.py

class Person:
    # 명사(속성)인 멤버변수
    name = '다현'
    age = 25
    weight = 57.0
    gender = 'female'


    # 초기화 메서드(파이썬 기본으로 포함)
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
    
    # def __str__(self): # 객체 출력을 문자열 포맷팅
    #     retStr = (self.name + '\n',
    #               str(self.age) + '\n',
    #               str(self.weight) + '\n',
    #               self.gender)
        #return retStr # 리턴 값이 튜플이라 오류 발생 
        # TypeError: __str__ returned non-string (type NoneType)
    def __str__(self):  
        return f"{self.name}\n{self.age}\n{self.weight}\n{self.gender}"

    # 동사(기상) 멤버함수(메서드드)
    # * 함수중에서 클래스 안에 속한 함수 메서드라고 한다(참고고)
    def getup(self): # myself
        print(f'{self.name}이(가) 일어납니다')
    
    def setWeight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')
    
    def getGender(self):
        return self.gender



man = Person('유고', 49, 78, 'male') # __init__() 특수함수를 실행
man.getup()
print(man.weight)
man.setWeight(55)
print(f'{man.name}의 성별은 {man.getGender()}.')
print('-------------------')
print('객체 정보')
print(man)