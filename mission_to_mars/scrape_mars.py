from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import pymongo


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # %%
    url = 'https://redplanetscience.com/'
    browser.visit(url)


    # %%
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # %%

    news_title = soup.find_all('div',class_='content_title')[0].text
    news_title


    # %%
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    news_p

    # %% [markdown]
    # ### JPL mars Space Images - Featured Image

    # %%
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # %%
    result = soup.find('div',class_='floating_text_area')
    result


    # %%
    link = result.find('a')['href']
    link
    featured_image = jpl_url + link
    featured_image

    # %% [markdown]
    # ### Mars Fact

    # %%
    mars_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(mars_url)
    mars = tables[0]
    


    # %%
    mars = mars.rename(columns={0:"", 1: 'Mars', 2:'Earth'})
    mars.set_index("",inplace=True)
    mars.drop(labels=["Mars - Earth Comparison"], axis=0,inplace=True)
    

    # %%
    html_table = mars.to_html()
    


    # %%
    html_string = html_table.replace('\n', '')
    
    

    # %% [markdown]
    # ### Mars Hemisphere

    # %%
    hems_url = 'https://marshemispheres.com/'
    browser.visit(hems_url)
    #html = browser.html
    # Parse HTML with Beautiful Soup
    #soup = BeautifulSoup(html, 'html.parser')


    # %%
    # get the name of the hemisphere, act 8 - day 2 - 
    #click name---get full image link
    #either create henisphere title or split


    # %%
    header = []
    link = []

    for x in range(4):
    # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
        result = soup.find_all('div',class_='description')[x]
        print(result)
        print('---------')
        title = result.find('h3').text
        header.append(title)
        print(title)
        print('---------')
        href = result.find('a')['href']
        link.append(href)
        print(href)
        print('---------')
        
        



        
        
        


    # %%
    header

   

    # %%
    link


    # %%
    full_image = []
    for x in link:
        image_link = hems_url + x
        print(image_link)
        browser.visit(image_link)
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all('div',class_='downloads')
        print(result)
        print('---------')
        
        for image in result:
            
            li =  image.find('li')
            print('---------')
            link2 = li.find('a')['href']
            print(link2)
            full_image.append(link2)

    print(full_image)

    image_url = []
    for url in full_image:
        full_link = hems_url + url
        image_url.append(full_link)
            
            
    
        
        


    # %%
    print(image_url)

    hemisphere_image_urls = []

    for i in range(4):
        hemisphere_image_urls.append({'title':header[i],'image_url':image_url[i]})

    hemisphere_image_urls

    # %%
    browser.quit()

    mars_dict= {}
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p
    mars_dict["featured_image_url"] = featured_image
    mars_dict["mars_facts"] = html_string
    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_dict


# %%
