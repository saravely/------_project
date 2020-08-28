import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# DB에 저장할 영화인들의 출처 url을 가져옵니다.
def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://gocamping.or.kr/bsite/camp/info/list.do', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#cont_inner > div > div.camp_search_list')

    urls = []
    for tr in trs:
        a = tr.select_one('ul > li:nth-child(1) > div > a')
        if a is not None:
            base_url = 'https://gocamping.or.kr/'
            url = base_url + a['href']
            urls.append(url)

    return urls


# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
def insert_camping(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    name = soup.select_one('#cont_inner > div > div.camp_search_list > ul > li:nth-child(1) > div > div > h2').text
    img_url = soup.select_one('#cont_inner > div > div.camp_search_list > ul > li:nth-child(1) > div > a > div > img')['src']
    text = soup.select_one('#cont_inner > div > div.camp_search_list > ul > li:nth-child(1) > div > div > span.camp_txt > a').text
    address = soup.select_one('#cont_inner > div > div.camp_search_list > ul > li:nth-child(1) > div > div > ul > li.addr').text
    call = soup.select_one('#cont_inner > div > div.camp_search_list > ul > li:nth-child(1) > div > div > ul > li.call_num').text

    doc = {
        'name': name,
        'img_url': img_url,
        'text': text,
        'address': address,
        'call': call
    }

    db.mycamping.insert_one(doc)
    print('완료!', name)


# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.campings.drop()  # mystar 콜렉션을 모두 지워줍니다.
    urls = get_urls()
    for url in urls:
        insert_camping(url)


## 실행하기
insert_all()