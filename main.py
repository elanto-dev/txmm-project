import sys
import argparse
import scraper.restaurants_scraper as scraper

def main():
    restaurant_info_csv = r"scraped_data\TripAdvisor_restaurants.csv"
    restaurant_reviews_csv = r"scraped_data\TripAdvisor_restaurants_reviews.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help ='need starting url')
    parser.add_argument('-i', '--info', action='store_true', help="Collects restaurant's info")
    parser.add_argument('-m', '--many', action='store_true', help="Collects whole area info")
    args = parser.parse_args()
    restaurant_url = args.url 
    #if you want to scrape restaurants info
    if args.info:
        scraper.scrape_restaurant_info(restaurant_url, restaurant_info_csv)

    scraper.scrape_restaurant_reviews(restaurant_url, restaurant_reviews_csv)

if __name__ == "__main__":
    main()