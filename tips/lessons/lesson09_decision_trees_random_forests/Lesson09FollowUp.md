## Lecture Follow Ups from Monday May 5th (Decision Trees)

#### What's the basic sklearn approach? Why do Ed and Dave keep using that word "modular"?
* sklearn is modular because the tools within sklearn are subsections of eachother
* This means all modules of sklearn fit patterns in coding
* By the end of the day, your code should always look like this implementing sklearn:

```python
import numpy as np
# All machine learning tools will live inside a library of sklearn
# This one is the DummyClassifier, which is a baseline classifier
from sklearn.dummy import DummyClassifier

# Split your data into the features you want to use (X) and what you're trying to predict (y)
X = np.array([[1, 2], [30, 40], [3, 4], [800, 100]])
y = np.array([0, 0, 1, 1])

# fit the classifier. Ultimately this can be any regressor or classifier class included in sklearn
clf = DummyClassifier().fit(X, y)

# All classifiers have the same outputs!
print clf.predict(X) #  This is also in regressions
print clf.predict_proba(X)
print clf.predict_log_proba(X)
print clf.score(X, y) # This is also in regressions

# Returns everything about how the classifier was created.
# This is useful in determining what is adjustable within the specific
# algorithm you are using.
print clf.get_params()
```

####Why do we cover what we cover in class? Is it integral to data science, or just one out of hundreds?
* The objective of the course is to expose you to the *most commonly implemented* algorithms data scientists use when working on a machine learning problem.
* That said, there is a [long list](http://en.wikipedia.org/wiki/List_of_machine_learning_algorithms) of [algorithms](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/) that exist!
* Consider using the [sklearn cheet sheet](http://1.bp.blogspot.com/-ME24ePzpzIM/UQLWTwurfXI/AAAAAAAAANw/W3EETIroA80/s1600/drop_shadows_background.png) to learn more about what to consider when understanding the process data scientists make in determining when to use one algorithm over another.
* Also consider looking at the "Road to becoming a Data Scientist" poster (included in this folder), which is a functional way of viewing all the "parts" to being a data scientist
* Dave and I are by no means experts in ALL of those things, and nor would ANY data scientist be. But we hope the class provides enough of a entry-level view to the data science world in order for you to find where your interests really lie in the field.

####We use so many things in sklearn! How do you know they exist? How do you figure out to use them?
* If you haven't yet, we highly recommend digging through the [sklearn documentation](http://scikit-learn.org/stable/documentation.html).
* In particular, the topics we have talked about/will talk about (alpha-order):
    * [Clustering](http://scikit-learn.org/stable/modules/clustering.html#clustering)
    * [Cross Validation](http://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
    * [Matrix Decomposition](http://scikit-learn.org/stable/modules/decomposition.html#decompositions)
    * [Ensemble Methods](http://scikit-learn.org/stable/modules/ensemble.html#ensemble)
    * [Feature Extraction](http://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction)
    * [Feature Selection](http://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)
    * [Linear Models](http://scikit-learn.org/stable/modules/linear_model.html#linear-model)
    * [Model Evaluation and Performance](http://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation)
    * [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html#naive-bayes)
    * [KNN](http://scikit-learn.org/stable/modules/neighbors.html#neighbors)
    * [Decision Trees](http://scikit-learn.org/stable/modules/tree.html#tree)
* From here, refer back to the sklearn graphic [above](http://1.bp.blogspot.com/-ME24ePzpzIM/UQLWTwurfXI/AAAAAAAAANw/W3EETIroA80/s1600/drop_shadows_background.png) as a starting point to understanding when to use what and when.

####Minimizing Gini vs Entropy in a decision tree for impurity
* Studies suggest that the difference in performance between these two (And others) is marginal.
* This is primarily because there is a correlation between Gini and Entropy, though they are scored differently
* Pruning a tree has significantly more impact than determining which to minimize
* To save on computation time, use Gini, since Entropy uses logs.

####What is the Receiving Operating Charateristic and AUC?
* This curve analyzes the performance of a binary classification problem
* Marking the four corners of the ROC space:
    - [Left, Bottom]: Represents where there were no false positives or true positives classified
    - [Left, Top]: (BEST!) Represents the space where no false positives were defined and all true positives where defined
    - [Right, Top]: Represents the space where all true positives where defined, but all negatives were also defined True
    - [Right, Bottom]: (WORST!) Represents the space where no true positives were found, and all negatives were defined True (inverse of what you want)
* fpr = false positives / (false positives + true negatives)
* tpr/recall = true positives / (true positives + false negatives)
* precision = true positives / (true positives + false positives)
* accuracy = (true positives + true negatives) / total observations

[Paper that breaks it all down](https://ccrma.stanford.edu/workshops/mir2009/references/ROCintro.pdf)

## Additional Assignments for Wednesday May 7
#### Final Project Brainstorm
* Review instructions for the [Final Project](https://github.com/datadave/GADS9-NYC-Spring2014-Lectures/blob/master/projects/FinalProject.md)
* Create a document in your student repo called "FinalProjectOutline.md" and include a few sentences in it on an idea or ideas you have for your final project.  Include:
	* What data set(s) you'd like to use
	* What questions you'd like to ask, classifiers you'd like to generate, and/or models you'd like to create
	* Any questions, concerns, or other ideas you might have related to the final project.

#### Project #2 Brainstorm
* Review instructions for [Project 2](https://github.com/datadave/GADS9-NYC-Spring2014-Lectures/blob/master/projects/project02.md)
* Create a document in your student repo called "Project2Outline.md" and include a) an idea of the dataset you'd like to look at b) the category or categories you'd like to predict.
