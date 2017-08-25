import requests
from bs4 import BeautifulSoup

def url_list():
    r = requests.get('http://paulgraham.com/articles.html')
    url_list = []
    url_soup = BeautifulSoup(r.text)
    for link in url_soup.tr.find_all('a'):
        url_list.append(link.get('href'))
    url_list = url_list[1:130] 
    return url_list



def get_text(url_list):
    f = open('graham.txt', 'w')

    for url in url_list:
        html = requests.get('http://paulgraham.com/'+url)    
        soup = BeautifulSoup(html.text)

        text = soup.table.get_text(' ')
        #text.encode('utf-8')

        f.write(text.encode('utf-8'))

    f.close()

def main():
    get_text(url_list())

main()