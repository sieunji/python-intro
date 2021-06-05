class Calculator(object): #object는 객체의미

    def __init__(self, first_num , second_num): #생성자인데 외부에서입력받는 값을 설정하는 메소드
        self.first_num  = first_num
        self.second_num = second_num

    def add(self): #더하기 메소드
        return self.first_num +self.second_num

    def sub(self):  # 빼기 메소드
        return self.first_num - self.second_num

    def mul(self):  # 곱하기 메소드
        return self.first_num * self.second_num

    def div(self):  # 나누기 메소드
        return self.first_num / self.second_num

    @staticmethod #일반 메소드에서 정의한 기능을 호출해서 실제값으로 연산하는 메소드를 스테틱메소드라고한다.
    def main():
        while 1: #1이란 참(true)을 의미. 따라서 연속으로 재실행한다는 의미
           menu= input('0-종료 1-계산기\n') #\n 한줄 띄워쓰기
           if menu == '0':
               break
           elif menu == '1':
               first_num = int(input('첫번째 수'))
               second_num = int(input('두번째 수'))
               calc =Calculator(first_num,second_num)  # first_num = 6, second_num  =2를 의미
               print('*'*30)
               print(f'{calc.first_num} + {calc.second_num} = {calc.add()}')
               print(f'{calc.first_num} - {calc.second_num} = {calc.sub()}')
               print(f'{calc.first_num} * {calc.second_num} = {calc.mul()}')
               print(f'{calc.first_num} / {calc.second_num} = {calc.div()}')
               print('*' * 30)
           else:
               print('잘못된 메뉴선택입니다.')

if __name__ == '__main__':
    Calculator.main()