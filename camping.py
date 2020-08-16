

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.google.com/search?q=kakao+%EC%A7%80%EB%8F%84+%EC%BA%A0%ED%95%91%EC%9E%A5&npsic=0&rflfq=1&rlha=0&rllag=37501365,127013538,14678&tbm=lcl&ved=2ahUKEwiSqeLu2JrrAhX0yYsBHdKbB54QjGp6BAgMEEM&rldoc=1#rlfi=hd:;si:;mv:[[38.072889599999996,127.72698150000001],[37.0645591,126.5932117]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:1')
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
for i in soup.select('#cont_inner > div > div.camp_search_list > ul > li') :
    print(i.select_one('div > div > div').text)
# document.querySelector("#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(1) > div > div.uMdZh.rl-qs-crs-t.mnr-c.rllt__local-item-selected > div > a > div > div.dbg0pd > div")
# base_url ='https://www.gocamping.or.kr/bsite/camp/info/list.do'
#
# for n in range(3):
#     url = base_url.format(n+1)
#     webpage = urlopen(url)
#     source = BeautifulSoup(webpage,'html5lib')
#     reviews = source.find_all('p',{'class':'i'})
#
#     for review in reviews :
#         print(i.get_text().strip)

# options = webdriver.ChromeOptions()
#
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
#
# driver = webdriver.Chrome('chromedriver', chrome_options=options)
#
# driver.implicitly_wait(3)
#
# l =['강원도 캠핑장','경기도 캠핑장','경상남도 캠핑장','경상북도 캠핑장','광주광역시 캠핑장','대구광역시 캠핑장','대전광역시 캠핑장']
#
# address=[]
# for idx in l:
#     driver.get('https://map.naver.com/')
#     driver.find_element_by_css_selector('#search-input').send_keys(idx)
#     driver.find_element_by_css_selector('#header button [type="submit').click()
#
#     while True:
#         html= driver.page_source
#         soup= bs(html,'html.parser')
#
#
# # url에 접근한다.
# driver.get('https://store.naver.com/accommodations/list?deviceType=pc&display=30&ip=121.135.232.67&query=%EC%BA%A0%ED%95%91%EC%9E%A5&region=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&sessionid=DQtYvA%2BAzFta%2BcdVRfpwdkSz&start=1')
#
# time.sleep(8)
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# print(soup)


