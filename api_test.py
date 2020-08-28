# from flask import Flask, render_template, jsonify, request
# from bs4 import BeautifulSoup
# import requests
# import json
# import pandas as pd
# import urllib
#
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
# with open('config.json', 'r') as f:
#     config = json.load(f)
#
# client_id = config['CLIENT_ID']  # 'secret-key-of-myapp'
# client_secret = config['CLIENT_SECRET'] # 개발자센터에서 발급받은 Client Secret 값
# API_KEY = config['KAKAO_REST_API_KEY']
#
# url = "https://dapi.kakao.com/v2/local/search/keyword.json "
# headers= {"Authorization" : 'KakaoAK ' + API_KEY}
# q = "캠핑장"
# params = {'query' : q }
#
# place = requests.get(url, params=params, headers=headers)

# API_KEY = config['KAKAO_REST_API_KEY']
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
# url= 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=127.423084873712&y=37.0789561558879&input_coord=WGS84'
# q = "캠핑장"
# params = {'query' : q }
# headers= {"Authorization" : 'KakaoAK ' + API_KEY}
# place = requests.get(url, params=params, headers=headers)
# # print(place.url)



# page = 1
# size = 50
#
# documents = []
# #상위 100건을 가져오기 위해서는 한 페이지당 50건씩 2 페이지의 분량을 수집해야 한다.
# for i in range(0,2):
#     page = i + 1
#     # API에 전달할 파라미터
#     params = {"page": page, "size": size, "query": q}
#     query = urllib.parse.urlencode(params)
#     api_url = url + "?" + query
#     print(query)

    # r = session.get(api_url)
    #
    # if r.status_code != 200:
    #     print("[%d Error] %s" % (r.status_code, r.reason))
    #     quit()
    # r.encoding = "utf-8"
    # book_dict = json.loads(r.text)




# params = {'query' : search_keyword, }
# headers= {"Authorization" : 'KakaoAK ' + API_KEY}
# place = requests.get(url, params=params, headers=headers)
# print(place.url)

# print(place.text)





#
# search_keyword = '가평 캠핑장'
# url = 'https://openapi.naver.com/v1/search/local'
#
# params = {'query' : search_keyword, 'display': 5,'start': 6}
#
# headers = {"X-Naver-Client-Id" : client_id, "X-Naver-Client-Secret" : client_secret}
# r = requests.get(url, params=params, headers=headers)

# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
#
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)




    # og_image = soup.select_one('meta[property="og:image"]')
    # og_title = soup.select_one('meta[property="og:title"]')
    # og_description = soup.select_one('meta[property="og:description"]')
    #
    # print(og_image)
    # print(og_title)
    # print(og_description)
    #
    # url_image = og_image['content']
    # url_title = og_title['content']
    # url_description = og_description['content']
    #
    # print(url_image)
    # print(url_title)
    # print(url_description)



    #
    # @app.route('/')
    # def home():
    #     return render_template('index.html')
    #
    #
    # @app.route('/memo', methods=['POST'])
    # def post_article():
    #     # 1. 클라이언트로부터 데이터를 받기
    #     url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
    #     comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
    #     # 2. meta tag를 스크래핑하기
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    #     data = requests.get(url_receive, headers=headers)
    #     soup = BeautifulSoup(data.text, 'html.parser')
    #
    #     og_image = soup.select_one('meta[property="og:image"]')
    #     og_title = soup.select_one('meta[property="og:title"]')
    #     og_description = soup.select_one('meta[property="og:description"]')
    #
    #     url_title = og_title['content']
    #     url_description = og_description['content']
    #     url_image = og_image['content']
    #     # 3. mongoDB에 데이터 넣기
    #     article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image,
    #                'comment': comment_receive}
    #     db.articles.insert_one(article)
    #
    #     return jsonify({'result': 'success'})
    #
    #
    # @app.route('/memo', methods=['GET'])
    # def read_articles():
    #     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    #     result = list(db.articles.find({}, {'_id': 0}))
    #     # 2. articles라는 키 값으로 articles 정보 보내주기
    #     return jsonify({'result': 'success', 'articles': result})
    #
    #
    # if __name__ == '__main__':
    #     app.run('127.0.0.1', port=5001, debug=True)