'''
키와 몸무게를 입력받아서 몸무게(70)/키(170)*키*10000
비만도 체크
'''
class Bmi(object):
    def __init__(self, height, weight): #몸무게와 키 값을 입력받는다는 뜻
        self.height = height
        self.weight = weight

    def get_bmi(self):
        index = self.weight /self.height ** 2 * 10000
        if index >= 35:
            bmi = '고도비만'
        elif index >= 30:
            bmi = '중도비만'
            
        elif index >= 25:
            bmi = '경도비만'
        
        elif index >= 23:
            bmi = '과체중'
            
        elif index >= 18.5:
            bmi = '정상'
        
        else:
            bmi = '저체중'

        return bmi

    @staticmethod
    def main():
        while 1:
            menu = input('0-종료 1-BMI\n')
            if menu == '0':
                break
            elif menu == '1':
                height = int(input('키 입력'))
                weight = int(input('몸무게 입력'))
                bmi = Bmi(height,weight)
                print(bmi.get_bmi())
            else:
                print('메뉴 다시 설정')
                continue

Bmi.main()