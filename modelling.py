import os
from gensim.models import LdaModel
from gensim import corpora
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors
from nltk.corpus import stopwords

def topic_modelling(sentences_list, file_name):
    clean_corpus = [sentence.split() for sentence in sentences_list]
    dictionary = corpora.Dictionary(clean_corpus)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in clean_corpus]
    lda = LdaModel(doc_term_matrix, num_topics=3, id2word = dictionary)
    num_topics = 10
    print(lda.print_topics(num_topics=num_topics, num_words=3))
    cols = [color for _, color in mcolors.TABLEAU_COLORS.items()]
    cloud = WordCloud(background_color='white',
                  width=2500,
                  height=1800,
                  max_words=10,
                  colormap='tab10',
                  color_func=lambda *args, **kwargs: cols[i],
                  prefer_horizontal=1.0)
    topics = lda.show_topics(formatted=False)
    fig, axes = plt.subplots(len(topics), 1, figsize=(10,10), sharex=True, sharey=True)
    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
        plt.gca().axis('off')


    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis('off')
    plt.title(file_name)
    plt.margins(x=0, y=0)
    plt.tight_layout()
    plt.show()
