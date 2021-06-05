from bs4 import BeautifulSoup
import requests

class Melon(object):
    url='https://www.melon.com/chart/index.htm?'
    headers ={'User-Agent':'Mozilla/5.0'} #멜론홈페이지 특이사항임
    class_name =[]

    def set_url(self,detail):
        #detail은 dayTime=2021060514 부분으로 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}',headers = self.headers).text #url 합치기

    def get_ranking(self):
        soup = BeautifulSoup(self.url,'lxml')
        ls1 = soup.find_all(name='div', attrs={"class":"ellipsis rank01"})
        for idx,title in enumerate(ls1): #index값을 가져오게 하는 함수: enumerate
            print(f'{idx+1}위 {title.find("a").text}')

    @staticmethod
    def main():
        melon = Melon()
        melon.set_url('dayTime=2021060514')
        melon.get_ranking()


Melon.main()