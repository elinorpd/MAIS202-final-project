import os
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import pickle
import nltk
from nltk.stem.snowball import SnowballStemmer


app = Flask(__name__)

global model
model = pickle.load(open('finalized_model.sav', 'rb'))

#create stemmer
stemmer = SnowballStemmer("english")

stop_words = ["", 'i', 'im', 'me', 'my', 'myself', 'we', 'our', 'ourselv', 'you$
                'your', 'youv', 'youll', 'youd', 'yourself', 'yourselv',
                'he', 'him', 'his', 'himself', 'she', 'shes', 'her', 'herself',
                'it', 'itself', 'they', 'them', 'their', 'themselv', 'what',
                'which', 'who', 'whom', 'this', 'that', 'thatll', 'these',
                'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'have',
                'has', 'had', 'do', 'doe', 'did', 'a', 'an', 'the', 'and', 'but$
                'if', 'or', 'becaus', 'as', 'until', 'while', 'of', 'at', 'by',
                'for', 'with', 'about', 'between', 'into', 'through', 'dure',
                'befor', 'after', 'abov', 'below', 'to', 'from', 'in', 'out',
                'on', 'off', 'over', 'under', 'further', 'then', 'onc', 'here',
                'there', 'when', 'where', 'whi', 'how', 'all', 'ani', 'both',
                'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
                'nor', 'not', 'onli', 'own', 'same', 'so', 'than', 'too', 'veri$
                's', 't', 'can', 'will', 'just', 'don', 'dont', 'should',
                'shouldv', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
                'aren', 'arent', 'couldn', 'couldnt', 'didn', 'didnt', 'doesn',
                'doesnt', 'hadn', 'hadnt', 'hasn', 'hasnt', 'haven', 'havent',
                'isn', 'isnt', 'ma', 'mightn', 'mightnt', 'mustn', 'mustnt',
                'needn', 'neednt', 'shan', 'shant', 'shouldn', 'shouldnt', 'was$
                'wasnt', 'weren', 'werent', 'won', 'wont', 'wouldn', 'wouldnt']

#clean function
def clean(content):
        content = str(content)
        words = content.split()
        list_of_words = []
        for i, word in enumerate(words):
                #make lowercase
                word = word.lower()
                #remove the links
                if ("http" not in word):
                        #keep the tags and mentions but get rid of punctuation
                        for char in word:
                                if (char != ' ') and (char != '@') and (char !=$
                                        word = word.replace(char, '')
                        #stem regular words
                        if ('@' not in word) and ('#' not in word):
                word = word.lower()
                #remove the links
                if ("http" not in word):
                        #keep the tags and mentions but get rid of punctuation
                        for char in word:
                                if (char != ' ') and (char != '@') and (char !=$
                                        word = word.replace(char, '')
                        #stem regular words
                        if ('@' not in word) and ('#' not in word):
                                word = stemmer.stem(word)
                        #remove stop words
                        if word not in stop_words:
                                list_of_words.append(word)
        return list_of_words #list of words - is essentially tokenized and stem$
global vectorizer
vectorizer = pickle.load(open('vectorizer1.sav', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def main_page():
        if request.method == 'POST':
                text = str(request.form['text'])
                return redirect(url_for('prediction', text=text))
        return render_template('index.html')

@app.route('/prediction/<text>')
def prediction(text):
        #create tweet
        #tweet = request.form['text']
        vectorized_tweet = vectorizer.transform([text])
        #predict category
        num_cat = model.predict(vectorized_tweet)
        if num_cat == 0:
                pred_cat = 'Commercial'
                info = '[These] handles engaged in commercial activity (four ma$
        elif num_cat == 1:
                pred_cat = 'Fearmonger'
                info = 'These accounts spread disinformation regarding fabricat$
        elif num_cat == 2:
                pred_cat = 'Hashtag Gamer'
                info = 'These handles are dedicated almost entirely to playing $
        elif num_cat == 3:
                pred_cat = 'Left Troll'
                info = 'These handles sent socially liberal messages, with an o$
        elif num_cat == 4:
                pred_cat = 'News Feed'
                info = 'These handles overwhelming presented themselves as U.S.$
        elif num_cat == 5:
                pred_cat = 'Nontroll'
                info = 'This is a dataset of tweets from various active scienti$
        elif num_cat == 6:
                pred_cat = 'Right Troll'
                info = 'These handles broadcast nativist and right-leaning popu$
        else:
                pred_cat = 'error' 
        #get confidence score matrix
        conf_score = model.decision_function(vectorized_tweet) [0]
        #find certainty of the predicted category
        certainty = round((np.amax(np.exp(conf_score)/sum(np.exp(conf_score)))*$
        result_string = ("This tweet is a " + str(pred_cat) + " tweet with " + $
        predictions = {"result":result_string, "info":info}
        return render_template('predict.html', predictions = predictions)
app.debug = True
app.run(host='0.0.0.0', port=80)

