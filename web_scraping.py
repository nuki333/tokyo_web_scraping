from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# リンク一括取得するWEBサイトを指定
url = 'https://www.metro.tokyo.lg.jp/link/link04.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
contents = soup.find(class_="row")
contents = soup.find(class_="col_main")
get_a = contents.find_all("a")

len(get_a)
alinks = []
for i in range(len(get_a)):
    try:
        link_ = get_a[i].get("href")
        alinks.append(link_)
    except:
        pass

df = pd.DataFrame(alinks)
df.to_csv('result\web_scraping_result.csv', index=False, encoding='utf-8-sig')