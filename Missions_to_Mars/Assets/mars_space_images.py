from bs4 import BeautifulSoup
from splinter import Browser


def mars_space_images(browser):

    # ### JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    #Click on Full Image link

    browser.click_link_by_partial_text('FULL IMAGE') 
    # Click on more info link
    browser.click_link_by_partial_text('more info') 
    
    #Find the image name
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    figure_link = soup.find('figure', class_="lede")
    link = figure_link.a['href']
    last_idx = link.rindex("/")
    Image_name = link[last_idx + 1:]

    # Click on the image
    browser.click_link_by_partial_href(Image_name)

    # Get th complete url string for this image
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.findAll('img')
    for image in images:
        featured_image_url = image['src']
    return featured_image_url