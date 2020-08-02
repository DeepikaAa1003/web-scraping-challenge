from bs4 import BeautifulSoup
import requests




# ### NASA Mars News
def mars_news(browser):
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    print(news_title)
    news_p_div = soup.find('div', class_='article_teaser_body')
    news_p = news_p_div.text
    print(news_p)
    news_dict = {"news_title": news_title, "news_p": news_p }
    return(news_dict)