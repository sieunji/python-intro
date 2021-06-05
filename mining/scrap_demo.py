from bs4 import BeautifulSoup

if __name__ == '__main__':
    html ='''
    <th scope="row">
        <p class="title" adult_yn="N">
        <a href="javascript:;" adultcheckval="1" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('32238640',true);
        " title="Butter" aria-label="새창">Butter</a>
        </p>
    </th>
    '''
    soup = BeautifulSoup(html,'html.parser')
    print(soup.title.string)