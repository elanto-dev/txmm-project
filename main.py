import scraper.scraper as scraper
import data_preprocessing.preprocessing as preprocessing
import data_preprocessing.common_restaurants_types as file_processing
import modelling
import argparse
import os
import glob


def main(scrape, remove_scraped, process_reviews):
    restaurant_info_csv = r"./scraped_data/TripAdvisor_restaurants.csv"
    restaurant_reviews_csv = r"./scraped_data/TripAdvisor_restaurants_reviews.csv"
    restaurant_reviews_cleaned_csv = r"./scraped_data/TripAdvisor_restaurants_reviews_cleaned.csv"
    restaurant_links_csv = r"tripadvisor_dutch_restaurants_links.csv"
    folder_name = "reviews"
    if scrape:
        print("scraping")
        #scraper.scrape_dutch_restaurants_data(restaurant_info_csv, restaurant_reviews_csv, restaurant_links_csv, remove_scraped)
    if process_reviews:
        print("Process scraped reviews and replace reviews folder content.")
        files_to_remove = glob.glob(f'./{folder_name}/*')
        for f in files_to_remove:
            os.remove(f)
        preprocessing.remove_duplicates(restaurant_reviews_csv, restaurant_reviews_cleaned_csv)
        most_common_restaurants_dict = file_processing.get_dict_of_most_common_types_of_restaurants(restaurant_info_csv, k_top_keys=5)
        file_processing.separate_reviews_to_files(restaurant_reviews_cleaned_csv, most_common_restaurants_dict, folder_name)
    new_files = glob.glob(f'./{folder_name}/*')
    for f in new_files:
        processed_reviews = preprocessing.read_and_preprocess_file(f)
        modelling.topic_modelling(processed_reviews, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scrape', action='store_true', help="Starts scraping process.")
    parser.add_argument('-r', '--remove_scraped', action='store_true', help="Remove scraped data.")
    parser.add_argument('-pr', '--process_reviews', action='store_true', help="Process reviews and replace folder content.")
    args = parser.parse_args()
    if args.scrape:
        scrape = True
    else:
        scrape = False
    if args.process_reviews:
        process_reviews = True
    else:
        process_reviews = False
    if args.remove_scraped:
        remove_scraped = True
    else:
        remove_scraped = False
    main(scrape, remove_scraped, process_reviews)