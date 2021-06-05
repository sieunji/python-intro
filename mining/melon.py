from bs4 import BeautifulSoup
import requests
import pandas as pd

class Melon(object):
    url='https://www.melon.com/chart/index.htm?'
    headers ={'User-Agent':'Mozilla/5.0'} #멜론홈페이지 특이사항임
    class_name =[]
    title_list = []
    artist_list = []
    dict = {}
    df = None

    def set_url(self,detail):
        #detail은 dayTime=2021060514 부분으로 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}',headers = self.headers).text #url 합치기

    def get_ranking(self):
        soup = BeautifulSoup(self.url,'lxml')
        t_list = soup.find_all(name='div', attrs={"class":"ellipsis rank01"})
        for idx,title in enumerate(t_list): #index값을 가져오게 하는 함수: enumerate
            print(f'{idx+1}위 {title.find("a").text}')
            self.title_list.append(title.find("a").text)

        print('=' * 100)

        a_list = soup.find_all(name='div', attrs={"class":"ellipsis rank02"})
        for artist in a_list: #index값을 가져오게 하는 함수: enumerate
            print(f'{artist.find("a").text}')
            self.artist_list.append(artist.find("a").text)

    def make_dict(self):
        for idx,title in enumerate(self.title_list):
            self.dict[title] = self.artist_list[idx]
            print(self.dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')

    def df_to_csv(self):
        path='./data/melon.csv'
        self.df.to_csv(path,sep=',',na_rep='NaN')

    @staticmethod
    def main():
        melon = Melon()
        melon.set_url('dayTime=2021060514')
        melon.class_name = ["title", "artist"]
        melon.get_ranking()
        melon.make_dict()
        melon.dict_to_dataframe()
        melon.df_to_csv()

Melon.main()