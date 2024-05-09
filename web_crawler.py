import requests as rq
from bs4 import BeautifulSoup

if __name__ == '__main__':
    def get_url(url):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/70.0.3538.102 Safari/537.36"}
        response = rq.get(url, headers=header).text
        soup = BeautifulSoup(response, 'lxml')
        response = soup.prettify()
        return response


    file = open('Bilibili_web.txt', 'w', encoding="utf-8")
    file.write(get_url('https://www.bilibili.com'))
