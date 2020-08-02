from bs4 import BeautifulSoup
import time

# ### Mars Hemispheres
def mars_hemi(browser):


        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(5)
        # Get 4 hemisphere headings as title
        results = soup.find('div', class_="collapsible results")
        Headings = results.findAll('h3')
        Image_title = []
        for heading in Headings:
            Image_title.append(heading.text)


        # Get image URL for 4 hemispehere

        Image_URL = []

        for image in Image_title:
            browser.click_link_by_partial_text(image)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            results = soup.find('div', class_="downloads")
            images = results.find('a')
            Image_URL.append(images['href'])
            browser.back()

        # Create a list of dictionaries
        hemisphere_image_urls = []
        for i in range(len(Image_title)):
            new_dict = {"title": Image_title[i], "img_url" : Image_URL[i]}
            hemisphere_image_urls.append(new_dict)
    
        return hemisphere_image_urls