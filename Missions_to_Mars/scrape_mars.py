from splinter import Browser
from bs4 import BeautifulSoup
import Assets.mars_news as mars_news
import Assets.mars_space_images as mars_space_images
import Assets.mars_weather as mars_weather
import Assets.mars_facts as mars_facts
import Assets.mars_hemispheres as mars_hemispheres


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    Final_Mars_dict = {}
    browser = init_browser()

   

    #Extract NASA Mars News
    news_dict = mars_news.mars_news(browser)
    Final_Mars_dict["news_title"] = news_dict["news_title"]
    Final_Mars_dict["news_p"] = news_dict["news_p"]

    browser.quit()

    # Extract JPL Mars Space Images - Featured Image
    browser = init_browser()

    featured_image_url = mars_space_images.mars_space_images(browser)
    Final_Mars_dict["featured_image_url"] = featured_image_url

    browser.quit()

    # ### Mars Weather

    browser = init_browser()

    mars_wth = mars_weather.weather(browser)
    Final_Mars_dict["mars_weather"] = mars_wth

    browser.quit()

    # ### Mars Hemispheres

    browser = init_browser()

    hemisphere_image_urls = mars_hemispheres.mars_hemi(browser)
    Final_Mars_dict["hemisphere_image_urls"] = hemisphere_image_urls
    print(Final_Mars_dict)

    browser.quit()

     # ### Mars Facts
    browser = init_browser()

    html_table = mars_facts.mars_facts()
    Final_Mars_dict["mars_facts"] = html_table

    browser.quit()

    print(Final_Mars_dict)
    

    return Final_Mars_dict
