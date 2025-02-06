# py02_car.py
# 객체지향 다시

class Car:
    ## __new__ 사용빈도x, __init__ 많이 사용
    ## Car() 호출하면 아래의 메서드가 실행
    ## company, name, plateNumber 모를 때는 None()
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company # 멤버변수 이름 앞에 __ 쓰면 외부접근 불가가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

    # 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    # return 반드시 해줘야 함
    def __str__(self):
        return f'제 차는 {self.__name}이고, 차 번호는 {self.__plateNumber}입니다'
    # 외부에서 잘못된 차 번호를 넣으면 안 들어감감
    def setPlateNumer(self, newPlateNumber):
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber

    def setName(self, newName='글쎄요'):
        if type(newName) is str:
            self.__name = newName

    def getName(self):
        return self.__name


# 모듈화 하기위해 예제 소스 주석처리

# myCar = Car('현대차', '아이오닉', '62로3306')
# 순서를 지키지 않아도 되는 경우 있음
# 파라미터 명을 반드시 써줘야 한다.
# myCar = Car(name='아이오닉', plateNumber='62로3306', company='현대차')

# print(myCar) # 차의 번호를 출력하고 싶음
# myCar.__plateNumber = '54라9537'
# print(myCar) # 클래스 외부에서 잘못된 데이터를 넣어도 문제 발생x
# myCar.setPlateNumer(2933)
# print(myCar)

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNumer('181버3834')
# print(yourCar)
# yourCar.setName()
# print(yourCar)
























































