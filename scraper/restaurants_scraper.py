import requests 
from bs4 import BeautifulSoup
import csv 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# This code was taken and adapted from GitHub repository: https://github.com/LaskasP/TripAdvisor-Python-Scraper-Restaurants-2021 

driver = webdriver.Chrome()

#webDriver init

def scrape_restaurant_info(url, file_path):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    restaurant_name = soup.find('h1', class_='HjBfq').text
    avg_rating = soup.find('span', class_='ZDEqb').text.strip()
    food_types = [x.text for x in soup.find_all('a', class_='dlMOJ') if all(chr.isalpha() or chr.isspace() for chr in x.text)]
    with open(file_path, mode='w', encoding="utf-8") as trip:
        data_writer = csv.writer(trip, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        data_writer.writerow([restaurant_name, avg_rating, food_types])

def scrape_restaurant_reviews(url, file_path):
    next_page = True
    while next_page:
        #Requests
        driver.get(url)
        time.sleep(1)
        #Click More button
        more = driver.find_elements("xpath", "//span[contains(text(),'More')]")
        for element in enumerate(more):
            try:
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
            except:
                pass
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #Store name
        storeName = soup.find('h1', class_='HjBfq').text
        #Reviews
        results = soup.find('div', class_='listContainer hide-more-mobile')
        try:
            reviews = results.find_all('div', class_='prw_rup prw_reviews_review_resp')
        except Exception:
            continue
        #Export to csv
        try:
            with open(file_path, mode='w', encoding="utf-8") as trip_data:
                data_writer = csv.writer(trip_data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                for review in reviews:
                    ratingDate = review.find('span', class_='ratingDate').get('title')
                    text_review = review.find('p', class_='partial_entry')
                    if len(text_review.contents) > 2:
                        reviewText = str(text_review.contents[0][:-3]) + ' ' + str(text_review.contents[1].text)
                    else:
                        reviewText = text_review.text
                    reviewerUsername = review.find('div', class_='info_text pointer_cursor')
                    reviewerUsername = reviewerUsername.select('div > div')[0].get_text(strip=True)
                    rating = review.find('div', class_='ui_column is-9').findChildren('span')
                    rating = str(rating[0]).split('_')[3].split('0')[0]
                    data_writer.writerow([storeName, reviewerUsername, ratingDate, reviewText, rating])
        except:
            pass
        #Go to next page if exists
        try:
            unModifiedUrl = str(soup.find('a', class_ = 'nav next ui_button primary',href=True)['href'])
            url = 'https://www.tripadvisor.com' + unModifiedUrl
        except:
            next_page = False





