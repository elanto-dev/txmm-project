import pandas as pd
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')  
nltk.download('omw-1.4')  
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import csv
from tokenize import tokenize

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def remove_duplicates(file_path, processed_file_path):
    columns = ["Restaurant name", "Author", "Date", "Review", "Rating"]
    data = pd.read_csv(file_path,names=columns)
    duplicateRowsDF = data[data['Review'].duplicated()]
    print(len(data))
    print("Found duplicates: " + str(len(duplicateRowsDF)) + ". Removing and writing to new file.")
    #Not working!
    cleaned_df = data.drop_duplicates(subset="Review")
    print(len(cleaned_df))
    cleaned_df.to_csv(processed_file_path, columns=columns, index=False)

# https://www.datacamp.com/tutorial/what-is-topic-modeling?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=157156373991&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=683184494156&utm_targetid=aud-517318241987:dsa-2218886984380&utm_loc_interest_ms=&utm_loc_physical_ms=9061552&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-dec23&gad_source=1&gclid=Cj0KCQiA1rSsBhDHARIsANB4EJZ-QZC0xEcsPF2fT0cluyTpxUXictSMIjqg11H3y7ZUMMunehnrxjMaAnO6EALw_wcB
def read_and_preprocess_file(file_path):
    reviews = []
    with open(file_path, mode='r', newline='', encoding="utf-8") as reviews_file:
        data_reader = csv.reader(reviews_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for review_list in data_reader:
            review = review_list[0]
            stop_free = " ".join([i for i in review.lower().split() if i not in stop])
            punc_free = "".join(ch for ch in stop_free if ch not in exclude)
            normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
            reviews.append(normalized)
    return reviews