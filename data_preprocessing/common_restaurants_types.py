import csv
import operator 
import itertools
from langdetect import detect

def get_dict_of_most_common_types_of_restaurants(file_path, k_top_keys = 5):
    with open(file_path, mode='r', newline='', encoding="utf-8") as restaurant_file:
        data_reader = csv.reader(restaurant_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        type_restaurant_dictionary = {}
        type_count_dictionary = {}
        for (restaurant_name, _, types) in data_reader:
            for ty in types.strip('][').split(', '):
                if ty: #Check string not null or empty
                    lower_case_type = ty.lower().replace("'", "")
                    if lower_case_type: 
                        if lower_case_type not in type_restaurant_dictionary.keys():
                            type_restaurant_dictionary[lower_case_type] = [restaurant_name]
                            type_count_dictionary[lower_case_type] = 1
                        else:
                            type_restaurant_dictionary[lower_case_type].append(restaurant_name)
                            type_count_dictionary[lower_case_type] += 1
        sorted_type_count_dictionary = dict(sorted(type_count_dictionary.items(), key=operator.itemgetter(1), reverse=True))
        top_keys = list(sorted_type_count_dictionary.keys())[:k_top_keys]
        result_dictionary = {}
        for key in top_keys:
            result_dictionary[key] = type_restaurant_dictionary[key]
        return result_dictionary
    
def separate_reviews_to_files(reviews_filepath, type_restaurant_dictionary, folder_name):
    all_restaurants_values = [x for xs in list(itertools.chain(type_restaurant_dictionary.values())) for x in xs]
    with open(reviews_filepath, mode='r', newline='', encoding="utf-8") as restaurant_file:
        data_reader = csv.reader(restaurant_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for (restaurant_name, author, date, review, rating) in data_reader:
            language = ""
            try:
                language = detect(review)
            except:
                print("Language was not identified, skipping restaurant: " + restaurant_name)
            if restaurant_name in all_restaurants_values and language == "en":
                keys_list = [k for k, v in type_restaurant_dictionary.items() if restaurant_name in v]
                for key in keys_list:
                    review = review.replace("\"", ""). replace("'", "")
                    if float(rating) > 3.0:
                        with open(fr"./{folder_name}/{key}_positive_reviews.csv", mode='a+', newline='', encoding="utf-8") as trip:
                            data_writer = csv.writer(trip, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                            data_writer.writerow([review])
                    elif float(rating) <= 3.0:
                        with open(fr"./{folder_name}/{key}_negative_reviews.csv", mode='a+', newline='', encoding="utf-8") as trip:
                            data_writer = csv.writer(trip, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                            data_writer.writerow([review])
                    else:
                        raise Exception('incorrect rating')


