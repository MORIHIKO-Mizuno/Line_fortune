from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

def get_fortune():
    try:
        # 最初のウェブページにアクセス
        html = urlopen("https://www.chunichi.co.jp/news/fortune")
    except HTTPError as e:
        return e  # エラーが発生した場合はエラーメッセージを返す
    except URLError as e:
        return e  # エラーが発生した場合はエラーメッセージを返す

    # BeautifulSoupを使ってページの情報を取得
    bs = BeautifulSoup(html.read(), "html.parser")
    link = bs.find("div", {"class": "content-area"}).find("a").attrs["href"]

    try:
        # リンク先のウェブページにアクセス
        html = urlopen("https://www.chunichi.co.jp" + link)
    except HTTPError as e:
        return e  # エラーが発生した場合はエラーメッセージを返す
    except URLError as e:
        return e  # エラーが発生した場合はエラーメッセージを返す

    # 再度 BeautifulSoupを使ってページの情報を取得
    bs = BeautifulSoup(html.read(), "html.parser")
    test = bs.find("div", {"class": "block"})

    # 正規表現を使って"☆ひつじ年"から始まる占い結果を抽出
    results = re.findall(r"☆ひつじ年.+?<br/>", str(test))
    result = results[0]
    result = result.replace("<br/>", "")
    result = result.replace("☆ひつじ年…", "")
    return result  # 抽出された占い結果を返す
