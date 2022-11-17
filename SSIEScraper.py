from urllib.request import urlopen
from bs4 import BeautifulSoup

def ScrapeExchangePage(url):

    requestPage = urlopen(url)
    pageHtml = requestPage.read()
    requestPage.close()

    htmlSoup = BeautifulSoup(pageHtml, 'html.parser')

    formattedArticles = []
    formattedArticlesWithTime = []

    class Article:
        def __init__(self, title, price, link, time):
            self.title = title
            self.price = price
            self.link = link
            self.time = time

    articles = htmlSoup.find_all('article')

    for article in articles:
        headers = article.find_all('header')
        for header in headers:
            price = header.find('div').text
            title = header.find('h2').text
            link = header.find('a', href=True)
            formattedArticles.append(Article(title, price, link['href'], 0))

    i=0
    for article in articles:
        uls = article.find_all('ul')
        for ul in uls:
            time = ul.find_all("li")[2].text
            formattedArticlesWithTime.append(Article(formattedArticles[i].title, formattedArticles[i].price, formattedArticles[i].link, time))
        
        i=i+1
        
    return formattedArticlesWithTime


