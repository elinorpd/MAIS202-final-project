# Tweet Classifier

Final project for McGill AI Society Intro to ML Bootcamp (Winter 2020). 

Troll tweet data retrieved from [this Kaggle dataset](https://www.kaggle.com/fivethirtyeight/russian-troll-tweets). 
Nontroll tweet data retrieved from [this Kaggle dataset](https://www.kaggle.com/speckledpingu/RawTwitterFeeds).

## Project description

This Tweet Classifier project is a web app that classifies text strings in the format of a tweet into one of 6 categories. I built the classification model using scikit-learn on Google Colab, utilizing a Stochastic Gradient Descent model. I made the web app using Flask.

## Running the model

First download your own kaggle.json file by going to the 'Account' tab of your user profile (`https://www.kaggle.com/<username>/account`) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials.

Open the final project file in [Google Colab](https://colab.research.google.com/drive/1wJbxyTvkjratU3H7LPFQ1rs3fzp5fgM6). Run all of the cells in order.


#### There are 5 sections in this collab notebook. 

The first is `Downloading Data`, where the kaggle datasets are downloaded and unzipped.
* Note that you will be prompted to upload the kaggle.json file in the first cell in order for it to download the datasets.

The second section is `Data Preprocessing`, where the datasets are merged and certain columns are removed. It will print the number of tweets in each category. Then, it cleans and vectorizes the data, as well as encodes the labels. This section takes approximately 6-8 minutes to run. If you would like to download the pickled vectorizer, uncomment the line ```files.download(filename)```.  

The third section is `Creating the model: Stochastic Gradient Descent`, where the model is trained and run on the test data. If you would like to download the pickled SGD model, uncomment the line ```files.download(filename)```.

The fourth section is ```Results```, where the accuracy metrics are calculated. It will print training and test accuracy, precision recall, and log loss. The confusion matrix is also plotted.

The fifth and final section is ```Predicting```, where the function that uses the model to classify a string of text is created. If you would like to try it on your own text, run ```result('your_text_here')``` in this section.

## Running the app

I followed [this tutorial](https://towardsdatascience.com/building-a-web-application-to-deploy-machine-learning-models-e224269c1331) in order to create the server in which to build the web app. If you want to recreate it, follow it and just replace all of the code for ```webapp.py``` and the ```index.html``` and ```predict.hmtl``` files with the ones here. In addition, you will also have to install nltk along with the other libraries in the tutorial using ```pip3 install nltk```.

My webapp link: http://192.241.151.161/

## Repository organization

This repository contains the scripts used to both train the model and build the web app.

1. deliverables/
	* deliverables submitted to the MAIS Intro to ML Bootcamp organizers
2. model/
	* final model, vectorizer, and Python file used to train the SGD model 
3. templates/
	* HTML template for landing and prediction page
4. webapp.py
	* main python script to instantiate Flask server
