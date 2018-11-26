import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    # __init__メソッドにスクレイピング対象になるWebサイトのURLを受け取る
    # 引数は任意
    def __init__(self, site):
        self.site = site    # インスタンス変数siteを定義する

    # scrapeメソッドでhtmlのスクレイピング結果を出力する
    def scrape(self):
        r = urllib.request.urlopen(self.site)   # urlopen関数でWebサイトへのリクエストを行う
        html = r.read() # htmlデータをResponseオブジェクトから返す(読み込む)  
        sp = BeautifulSoup(html, 'html.parser')  # html変数とhtml.parserを引数として渡し、BSのオブジェクトを作成する
        # find_allメソッドで<a>タグを全て集める  
        for tag in sp.find_all('a'):    # htmlにfind_allして'a'に一致するTagオブジェクトがtagに代入される
            url = tag.attrs['href'] # urlのみをリスト形式で取り出す
            title = tag.string  # 説明テキストを取り出す
            print(title, '>', url)  # 出力する



news = 'https://news.google.com/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnFZUm9DU2xBb0FBUAE?hl=ja&gl=JP&ceid=JP%3Aja'    
Scraper(news).scrape()  # Scraperオブジェクトを作成し、scrapeメソッドを実行する