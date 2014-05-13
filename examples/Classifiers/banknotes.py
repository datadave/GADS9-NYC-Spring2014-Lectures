#!/usr/bin/env python
"""
Simple code to show classification algorithms in action.

Written for GADS9-NYC-Spring2014
"""

# Import pandas and a helper routine to split data into training and test sets
import pandas as pd
from sklearn.cross_validation import train_test_split

# Import our models
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier

def runClassifier(clf,title,xtrain,ytrain,xtest,ytest):
    """
    Trains a classification model and prints an accuracy
    score when predicting labels for test data.

    Inputs:
        clf - an instantiated classification object
        title - a string to refer to the classification algorithm
        xtrain - training dataset
        ytrain - training labels
        xtest - testing dataset
        ytest - testing labels
    """
    # train the model using the classifier's fit function
    # use a dummy variable to avoid gibberish being printed
    clf.fit(xtrain, ytrain)

    # use the model to predict labels for the test set
    # note: this step is redundant if you just want the score
    #predictions = clf.predict(xtest)

    # the score function will run the predict method and then calculate
    # the accuracy based on the labels it calculates and the actual labels
    score = clf.score(xtest, ytest)

    # print the accuracy of our model on the test data
    print "%s Accuracy: %0.2f%%" % (title,(100.0 * score))

    # return the predictions in case the caller is interested
    #return predictions
# end of runClassifier()

def main(filename):
    # read the file into a pandas DataFrame object
    df = pd.read_csv(filename)

    # This particular dataset lacks a header
    # Let's tell pandas what the columns are (see the link below)
    # https://archive.ics.uci.edu/ml/datasets/banknote+authentication
    df.columns = ['variance','skewness','curtosis','entropy','class']
    
    # print the first 3 rows to show the user what the data looks like
    print ""
    print "First three rows of the data"
    print "----------------------------"
    print df.head(3)
    print ""

    # create X and Y for (using all features for X)
    # I like defining a list of features (above) to easily test changes
    features = ['variance','skewness','curtosis','entropy']
    X = df[features]
    Y = df['class']

    # use sklearn to build the training and test sets
    # note the order in which it returns variables!
    xtrain, xtest, ytrain, ytest = train_test_split(X,Y)

    classifiers = {
        'Bernoulli Naive Bayes':BernoulliNB(),
        'Gaussian Naive Bayes':GaussianNB(),
        'Logistic Regression':LogisticRegression(),
        'K-Nearest Neighbors':KNeighborsClassifier(n_neighbors=3,weights='uniform')}

    for title, clf in classifiers.items():
        runClassifier(clf,title,xtrain,ytrain,xtest,ytest)

    # end with a blank line for readability
    print ""
# end of main()

if __name__=="__main__":
    main('data_banknote_authentication.txt')
# end of file
