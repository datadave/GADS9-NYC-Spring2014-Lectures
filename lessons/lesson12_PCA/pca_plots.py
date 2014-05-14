





#!/usr/local/bin/python
"""
=======================================================
Comparison of LDA and PCA 2D projection of Iris dataset
=======================================================

The Iris dataset represents 3 kind of Iris flowers (Setosa, Versicolour
and Virginica) with 4 attributes: sepal length, sepal width, petal length
and petal width.

Principal Component Analysis (PCA) applied to this data identifies the
combination of attributes (principal components, or directions in the
feature space) that account for the most variance in the data. Here we
plot the different samples on the 2 first principal components.

Linear Discriminant Analysis (LDA) tries to identify attributes that
account for the most variance *between classes*. In particular,
LDA, in constrast to PCA, is a supervised method, using known class labels.
"""
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn.svm import LinearSVC

def scree_plot():
    # center data (important for dim reduction)
    iris = datasets.load_iris()
    iris.data = iris.data - np.mean(iris.data, axis=0)
    
    # get covariance matrix
    np.cov(iris.data).shape         # this has the wrong dimensions
    np.cov(iris.data, rowvar=0).shape   # this is good
    
    iris_cov = np.cov(iris.data, rowvar=0)
    
    # eigenvalue decomp
    iris_eig = np.linalg.eig(iris_cov)
    iris_egval = iris_eig[0]
    
    # pct of variance explained by each principal component
    pcts = [k/sum(iris_egval) for k in iris_egval]
    
    plt.plot(pcts)
    plt.xlabel('principal cmpts')
    plt.ylabel('pct variance explained')
    plt.title('iris scree plot')
    plt.show()

def pca_plot():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names
    
    pca = PCA(n_components=2)
    X_decomp = pca.fit(X).transform(X)
    
    print 'explained variance ratio (first two components):', \
        pca.explained_variance_ratio_
    
    pl.figure()
    for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
        pl.scatter(X_decomp[y == i, 0], X_decomp[y == i, 1], c=c, label=target_name)
    pl.legend()
    pl.title('PCA of IRIS dataset')
    pl.show()

if __name__ == '__main__':
    # scree_plot()
    pca_plot()
