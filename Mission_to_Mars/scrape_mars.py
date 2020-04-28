from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def init_browser(url):
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=True)
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = bs(html,'html.parser')
    soup.prettify()
    
    return soup


def scrapeLatestNewsTitleAndPara(dictionary):

    url = "https://mars.nasa.gov/news/"
    soup = init_browser(url)
    # Get list of all the headlines
    headline_lists= soup.find('ul', class_="item_list")

    # Collect top headline and title from list of headlines 
    latest_headline_title = headline_lists.find('div', class_="content_title").text
    latest_headline_para = headline_lists.find('div', class_="article_teaser_body").text


    dictionary['latest_headline_title'] = latest_headline_title
    dictionary['latest_headline_para'] = latest_headline_para

    return dictionary

def scrapeMarsFeaturedImage(dictionary):

  
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    soup = init_browser(url)

    # Extract tag containing url to latest url to current featured mars image
    article = soup.find('article', class_="carousel_item")

    # Extract url from the article tag
    start = article['style'].find("/")
    end = article['style'].find("\')")
    featured_image_url = "https://www.jpl.nasa.gov" + article['style'][start:end]

    dictionary['mars_featured_image_url'] = featured_image_url

    return dictionary

def scrapeLatestMarsWeatherTweet(dictionary):

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    soup = init_browser(weather_url)
    
    result = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
    mars_weather_tweet = result.find('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").text.strip()

    dictionary['weather_tweet'] = mars_weather_tweet

    return dictionary

def scrapeMarsFacts(dictionary):

    mars_facts_url = "https://space-facts.com/mars/"
    soup = init_browser(mars_facts_url)
    
    tables = pd.read_html(mars_facts_url)
    mars_facts_df = tables[0]

    html_table = mars_facts_df.to_html(index=False,header=False)
    html_table = html_table.replace('\n', '')

    dictionary['mars_facts'] = html_table

    return dictionary

def scrapeHemisphereTitleAndImageUrls(dictionary):

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    soup = init_browser(usgs_url)

    item_list = soup.find_all('div', class_='item')

    base_url = "https://astrogeology.usgs.gov"
    
    hemisphere_image_urls = []
    for item in item_list:
        anchor_tag = item.find('a', class_='itemLink product-item')
        
        image_title = item.find('h3').text.strip().split(' Enhanced')[0]
        url = base_url + anchor_tag['href']
        
        # Navigate to new url to fetch url of high res image
        soup = init_browser(url)
        
        full_res_image_url = soup.find('div', class_="downloads").find_all('li')[1].find('a')['href']
        hemisphere_image_urls.append({"image_title": image_title,"img_url": full_res_image_url})
       
    
    
    dictionary['hemisphere_image_url_list'] = hemisphere_image_urls
            
    return dictionary


def scrape():
    dictionary = {}

    dictionary = scrapeLatestNewsTitleAndPara(dictionary)
    dictionary = scrapeMarsFeaturedImage(dictionary)
    dictionary = scrapeLatestMarsWeatherTweet(dictionary)
    dictionary = scrapeMarsFacts(dictionary)
    dictionary = scrapeHemisphereTitleAndImageUrls(dictionary)
 
    print(dictionary['latest_headline_title'])
    print(dictionary['latest_headline_para'])
    print('*********************************************************************************')
    print(dictionary['mars_featured_image_url'])
    print('*********************************************************************************')
    print(dictionary['mars_facts'])
    print('*********************************************************************************')
    print(dictionary['hemisphere_image_url_list'])


    return dictionary
