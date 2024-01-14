import scraper.restaurants_scraper as scraper
import scraper.tripadvisor_european_restaurants_data_processing as restaurants_link_data_processer
import csv
import os

def scrape_dutch_restaurants_data(restaurant_info_csv, restaurant_reviews_csv, restaurant_links_csv, remove_scraped):
    # Uncomment the following lines to rewrite the scraped data. 
    """restaurants_link_data_processer.read_restaurants_csv("./scraper/tripadvisor_european_restaurants.csv", restaurant_links_csv)
    if remove_scraped:
        if os.path.exists(restaurant_info_csv):
            os.remove(restaurant_info_csv)
        if os.path.exists(restaurant_reviews_csv):
            os.remove(restaurant_reviews_csv)"""
    with open(restaurant_links_csv, mode='r', newline='', encoding="utf-8") as links_input:
        data_reader = csv.reader(links_input, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for restaurant_link in data_reader:
            restaurant_has_reviews = scraper.scrape_restaurant_info(restaurant_link[0], restaurant_info_csv)
            if restaurant_has_reviews:
                scraper.scrape_restaurant_reviews(restaurant_link[0], restaurant_reviews_csv)
