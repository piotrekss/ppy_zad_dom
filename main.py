import webbrowser
import requests
if __name__ == '__main__':

    url = "http://archive.org/wayback/available?url=" + "http://www.mediaexpert.pl/" + "&timestamp=" + str("20160801")
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

url = "http://archive.org/wayback/available?url=" + "http://www.spryciarze.pl/" + "&timestamp=" + str("20081104")
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

url = "http://archive.org/wayback/available?url=" + "http://www.canalplus.pl/" + "&timestamp=" + str("20190903")
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)




