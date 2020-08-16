from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import json

url = 'https://platum.kr/archives/120958'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta



import os
import sys
import urllib.request

with open('config.json', 'r') as f:
    config = json.load(f)

client_id = config['CLIENT_ID']  # 'secret-key-of-myapp'

client_secret = config['CLIENT_SECRET'] # 개발자센터에서 발급받은 Client Secret 값


encText = urllib.parse.quote("https://developers.naver.com/docs/utils/shortenurl")
data = "url=" + encText
url = "https://openapi.naver.com/v1/util/shorturl"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)




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