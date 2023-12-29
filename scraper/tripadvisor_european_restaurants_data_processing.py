import csv 

def read_restaurants_csv(file_path, output_file):
    with open(file_path, mode='r', newline='', encoding="utf-8") as input, \
         open(output_file, mode='w', newline='', encoding="utf-8") as output:
        # Initialise reader and writer 
        data_reader = csv.reader(input, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        data_writer = csv.writer(output, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

        # Read data, process and write into the output file
        for e, (restaurant_link,restaurant_name,orig_location,country,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_) in enumerate(data_reader):
            if country == "The Netherlands" and e: # Only process restaurants located in the Netherlands
                # Replace special symbols with underscore for correct links 
                restaurant_name = restaurant_name.replace(" ", "_").replace('"', "").replace("\'", "_").replace(",", "_")
                orig_location = orig_location.strip('][').split(', ')
                if len(orig_location) == 5:
                    province = orig_location[2].replace(" ", "_").replace('"', "")
                    municipality = orig_location[3].replace(" ", "_").replace('"', "")
                    city = orig_location[4].replace(" ", "_").replace('"', "")
                    link = f"https://www.tripadvisor.com/Restaurant_Review-{restaurant_link}-Reviews-{restaurant_name}-{city}_{municipality}_{province}.html".replace("__", "_")
                    data_writer.writerow([link])
                if len(orig_location) == 4:
                    province = orig_location[2].replace(" ", "_").replace('"', "")
                    city = orig_location[3].replace(" ", "_").replace('"', "")
                    link = f"https://www.tripadvisor.com/Restaurant_Review-{restaurant_link}-Reviews-{restaurant_name}-{city}_{province}.html".replace("__", "_")
                    data_writer.writerow([link])