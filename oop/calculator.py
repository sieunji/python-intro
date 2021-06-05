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
       calc =Calculator(6,2)  # first_num = 6, second_num  =2를 의미
       print('*'*30)
       print(f'{calc.first_num} + {calc.second_num} = {calc.add()}')
       print(f'{calc.first_num} - {calc.second_num} = {calc.sub()}')
       print(f'{calc.first_num} * {calc.second_num} = {calc.mul()}')
       print(f'{calc.first_num} / {calc.second_num} = {calc.div()}')
       print('*' * 30)

if __name__ == '__main__':
    Calculator.main()