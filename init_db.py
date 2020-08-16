import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://store.naver.com/accommodations/list?ip=121.135.232.67&isService=true&page=1&query=%EC%BA%A0%ED%95%91%EC%9E%A5&region=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&so=rel.dsc', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')

    urls = []
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls

def insert_star(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    recent_work = soup.select_one(
        '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

    doc = {
        'name': name,
        'img_url': img_url,
        'recent': recent_work,
        'url': url,
        'like': 0
    }

    db.mystar.insert_one(doc)
    print('완료!', name)

    def insert_all():
        db.mystar.drop()  # mystar 콜렉션을 모두 지워줍니다.
        urls = get_urls()
        for url in urls:
            insert_star(url)

    ### 실행하기
    insert_all()