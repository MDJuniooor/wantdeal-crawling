# Crawling Server For WantDeal

## 개발환경
- python 3.7.3
- django 3.1.4
- scrapy 2.4.1
- scrapy-djangoitem 1.1.1
- pillow 8.0.1

## 실행방법
1. 디펜던시 설치
```
pip install -r requiremenets.txt
```
2. django 서버 실행
```
python manage.py runserver
```
3. crawling 실행
```
# 뽐뿌 크롤링 실행
scrapy crawl bbombbu

# 딜바다 크롤링 실행
scrapy crawl dealbada
```



## 1.0 version
###  크롤링 상세
- 타겟 : 뽐뿌, 딜바다
- 내용 : 딜 제목, 카테고리, url, 이미지 

### 새로운 상품 추가를 위한 전략
1. 10분 Or 20분 단위로 크롤링
2. 각 사이트 게시글의 id를 읽어서 중복인 것은 Error

### 개선사항
- 베타버전으로 가격 추출이 안됨
- 동일한 요건으로 제목만 추출하고 상품 추출이 안됨