import scraper.scraper as scraper
import argparse
import os
import glob


def main(scrape, remove_scraped):
    restaurant_info_csv = r"./scraped_data/TripAdvisor_restaurants.csv"
    restaurant_reviews_csv = r"./scraped_data/TripAdvisor_restaurants_reviews.csv"
    restaurant_links_csv = r"tripadvisor_dutch_restaurants_links.csv"
    if scrape:
        print("Start scraping process")
        scraper.scrape_dutch_restaurants_data(restaurant_info_csv, restaurant_reviews_csv, restaurant_links_csv, remove_scraped)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scrape', action='store_true', help="Starts scraping process.")
    parser.add_argument('-r', '--remove_scraped', action='store_true', help="Remove scraped data.")
    args = parser.parse_args()
    scrape = False
    if args.scrape:
        scrape = True
    remove_scraped = False
    if args.remove_scraped:
        remove_scraped = True
    main(scrape, remove_scraped)