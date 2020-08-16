import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# DB에 저장할 영화인들의 출처 url을 가져옵니다.
def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://store.naver.com/accommodations/list?deviceType=pc&display=30&ip=116.37.34.148&query=%EC%BA%A0%ED%95%91%EC%9E%A5',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#container > div > div > div > div > ul > li')

    urls = []
    for tr in trs:
        a = tr.select_one('div > div > div > span > a ')
        if a is not None:
            base_url = 'https://store.naver.com/accommodations/list?deviceType=pc&display=30&ip=116.37.34.148&query=%EC%BA%A0%ED%95%91%EC%9E%A5'
            url = base_url + a['href']
            urls.append(url)

    return urls


def insert_camping(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://store.naver.com/accommodations/list?deviceType=pc&display=30&ip=116.37.34.148&query=%EC%BA%A0%ED%95%91%EC%9E%A5',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

   name = soup.select_one("#_business_19963724 > div > div > div.tit > span > a > span").text

# --------------------------------------------------------------
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://store.naver.com/accommodations/list?deviceType=pc&display=30&ip=116.37.34.148&query=%EC%BA%A0%ED%95%91%EC%9E%A5')
#
#
# soup = BeautifulSoup(browser.page_source,'html.parser')
# for name in soup.select('#container > div > div > div > div > ul > li'):
#     print(name.select_one('div > div > div > span > a > span').text)
#
# for address in soup.select('#container > div > div > div > div > ul > li'):
#     print(address.select_one('list_item_inner > info_area > txt ellp').text)

# ----------------------------------------------------------------------------


# for i in soup.select('#container > div > div > div > div > ul > li','html.parser')

# for detail in details:
#     a_tag = detail.select_one('div > div > div > span > a')
#     if a_tag is not None:
#         name = a_tag.text
#         address = detail.select_one('txt ellp')
#         price = detail.select_one('txt price')
#
#         print('name, address, price')


# print(i.select_one('div > div > div > span > a > span').text)


# ------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#
# class craigslist_crawler(object):
#     def __init__(self,query,region):
#         self.region = region
#         self.query = query
#         self.url = f"https://store.naver.com/accommodations/list?deviceType=pc&display=30&ip=116.37.34.148&query={query}region={region}"
#         self.driver = webdriver.Chrome("Driverchromedriver.exe")
#         self.delay = 5
#
#         def load_page(self):
#             driver = self.driver
#             driver.get(self.url)
#             all_data = driver.find_element_by_class_name("info_area")
#             for data in all_data:
#                 print(data.text) # name, price, description
#
#
# query = "캠핑장"
# region = "경기도"
# crawler = craigslist_crawler(query,region)
# crawler.load_page()

# --------------------------------------------------------


# import time
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome('chromedriver')

#
# for i in range(1) :
#     print('https://www.gocamping.or.kr/bsite/camp/info/list.do?pageUnit=10&searchKrwd=&listOrdrTrget=last_updusr_pnttm&pageIndex=' + str(i))
#     url = 'https://www.gocamping.or.kr/bsite/camp/info/list.do?pageUnit=10&searchKrwd=&listOrdrTrget=last_updusr_pnttm&pageIndex=' + str(i)
#
#     driver.implicitly_wait(3)
#     # url에 접근한다.
#     driver.get(url)
#     time.sleep(3)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#
#     for i in soup.select('#cont_inner > div > div.camp_search_list > ul > li'):
#         print(i.select_one('div > div > h2').text)

# for a in soup.select('#cont_inner > div > div.camp_search_list > ul > li'):
#     print(a.select_one('div > div > ul').text)
