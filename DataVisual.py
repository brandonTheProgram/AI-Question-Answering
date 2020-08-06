#python -m spacy download en_core_web_sm    This is needed to use the model
#Link https://www.machinelearningplus.com/nlp/topic-modeling-visualization-how-to-present-results-lda-models/#9.-Word-Clouds-of-Top-N-Keywords-in-Each-Topic
from FileConverters import *
import sys
import re, numpy as np, pandas as pd
import gensim, spacy, logging, warnings
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Canvas(FigureCanvas):
    #Create a canvas for a graph to be drawn on
    def __init__(self, parent = None):
        self.figure = plt.figure(figsize=(16,7), dpi=160)
        self.canvas = FigureCanvas(self.figure)
 
        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)

    #Load in the data and display the visual
    def DisplayVisual(self, fileList):
        # NLTK Stop words
        stop_words = stopwords.words('english')
        stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come'])

        warnings.filterwarnings("ignore",category=DeprecationWarning)
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

        def sent_to_words(sentences):
            for sent in sentences:
                sent = re.sub('\S*@\S*\s?', '', sent)  # remove emails
                sent = re.sub('\s+', ' ', sent)  # remove newline chars
                sent = re.sub("\'", "", sent)  # remove single quotes
                sent = gensim.utils.simple_preprocess(str(sent), deacc=True) 
                yield(sent)

        data = []

        # Add the data from the list
        for file in fileList:
            if file[-3:] == "pdf":
                data.append(pdf2_to_text(file))
            elif file[-4:] == "docx":
                data.append(docx2_to_txt(file))
            else:
                try:
                    with open(file, "r") as f:
                        data.append(f.read())
                except Exception as err:
                    LogError(err, file)
                    
        data_words = list(sent_to_words(data))

        # Build the bigram and trigram models
        bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
        trigram = gensim.models.Phrases(bigram[data_words], threshold=100)  
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        trigram_mod = gensim.models.phrases.Phraser(trigram)

        def process_words(texts, stop_words=stop_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
            """Remove Stopwords, Form Bigrams, Trigrams and Lemmatization"""
            texts = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
            texts = [bigram_mod[doc] for doc in texts]
            texts = [trigram_mod[bigram_mod[doc]] for doc in texts]
            texts_out = []
            try:
                nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
                nlp.max_length = 2000000
                for sent in texts:
                    doc = nlp(" ".join(sent)) 
                    texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
                # remove stopwords once more after lemmatization
                texts_out = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts_out]
            except Exception as err:
                LogError(err, file)
            return texts_out

        # processed Text Data!
        data_ready = process_words(data_words)  

        # Create Dictionary
        id2word = corpora.Dictionary(data_ready)

        # Create Corpus: Term Document Frequency
        corpus = [id2word.doc2bow(text) for text in data_ready]

        # Build LDA model
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=4, 
                                                random_state=100,
                                                update_every=1,
                                                chunksize=10,
                                                passes=10,
                                                alpha='symmetric',
                                                iterations=100,
                                                per_word_topics=True)

        def format_topics_sentences(ldamodel=None, corpus=corpus, texts=data):
            # Init output
            sent_topics_df = pd.DataFrame()

            # Get main topic in each document
            for i, row_list in enumerate(ldamodel[corpus]):
                row = row_list[0] if ldamodel.per_word_topics else row_list            
                # print(row)
                row = sorted(row, key=lambda x: (x[1]), reverse=True)
                # Get the Dominant topic, Perc Contribution and Keywords for each document
                for j, (topic_num, prop_topic) in enumerate(row):
                    if j == 0:  # => dominant topic
                        wp = ldamodel.show_topic(topic_num)
                        topic_keywords = ", ".join([word for word, prop in wp])
                        sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
                    else:
                        break
            sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

            # Add original text to the end of the output
            contents = pd.Series(texts)
            sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
            return(sent_topics_df)

        df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=data_ready)

        # Format
        df_dominant_topic = df_topic_sents_keywords.reset_index()
        df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']

        # Display setting to show more characters in column
        pd.options.display.max_colwidth = 100

        sent_topics_sorteddf_mallet = pd.DataFrame()
        sent_topics_outdf_grpd = df_topic_sents_keywords.groupby('Dominant_Topic')

        for i, grp in sent_topics_outdf_grpd:
            sent_topics_sorteddf_mallet = pd.concat([sent_topics_sorteddf_mallet, 
                                                    grp.sort_values(['Perc_Contribution'], ascending=False).head(1)], 
                                                    axis=0)

        # Reset Index    
        sent_topics_sorteddf_mallet.reset_index(drop=True, inplace=True)

        # Format
        sent_topics_sorteddf_mallet.columns = ['Topic_Num', "Topic_Perc_Contrib", "Keywords", "Representative Text"]

        doc_lens = [len(d) for d in df_dominant_topic.Text]

        # Plot the data
        self.figure.clear()
        plt.hist(doc_lens, bins = 1000, color='navy')
        plt.text(750, 100, "Mean   : " + str(round(np.mean(doc_lens))))
        plt.text(750,  90, "Median : " + str(round(np.median(doc_lens))))
        plt.text(750,  80, "Stdev   : " + str(round(np.std(doc_lens))))
        plt.text(750,  70, "1%ile    : " + str(round(np.quantile(doc_lens, q=0.01))))
        plt.text(750,  60, "99%ile  : " + str(round(np.quantile(doc_lens, q=0.99))))

        plt.gca().set(xlim=(0, 1000), ylabel='Number of Documents', xlabel='Document Word Count')
        plt.tick_params(size=16)
        plt.xticks(np.linspace(0,1000,9))
        plt.title('Distribution of Document Word Counts', fontdict=dict(size=22))

        # refresh canvas
        self.canvas.draw()
