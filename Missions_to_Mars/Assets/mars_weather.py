from bs4 import BeautifulSoup
import time

# ### Mars Weather
def weather(browser):
    
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)

    # find the latest tweet and get the span having text starting with word "InSight"
    results = soup.find("div", { "data-testid" : "tweet" })
    for result in results:
        print(result)
        spans = result.findAll('span')
        for span in spans:
            print(span)
            if(span.text.startswith("InSight")):
                mars_weather_text  = span.text
 
    return mars_weather_text