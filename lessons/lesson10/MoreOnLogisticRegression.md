# Logistic Regression / Classification Review


Logistic Regression is a function approximation algorithm that uses training data to directly estimate P(Y|X), in contrast to Naive Bayes. In this sense,
Logistic Regression is often referred to as a discriminative classiﬁer because we can view the distribution P(Y|X) as directly discriminating the value of the target value Y for any given instance X

Logistic Regression is a linear classifier over X. The linear classifiers pro- duced by Logistic Regression and Gaussian Naive Bayes are identical in the limit as the number of training examples approaches infinity, provided the Naive Bayes assumptions hold. However, if these assumptions do not hold, the Naive Bayes bias will cause it to perform less accurately than Lo- gistic Regression, in the limit. Put another way, Naive Bayes is a learning algorithm with greater bias, but lower variance, than Logistic Regression. If this bias is appropriate given the actual data, Naive Bayes will be preferred. Otherwise, Logistic Regression will be preferred.
(source: [Tom Mitchell](http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf)


## Key Points
* "Logistic" due to special mathematical function
* "Regression" because it combines a weight factor with observations.

We estimate probabilities for Y=0 and Y=1 given X with the following functions:
![](http://note.io/1sFExtq)

or, by removing the logistic function:
![](http://note.io/1sFEY79)

from the equation, we can use:
![](http://note.io/1sFJJNX)

We might also consider how logistic regression equations are linear in the logit scale:

![](http://note.io/1sFQdwr)

#### Example:
![](http://note.io/1sFH4nq)

We'll let Y=1 indicate spam.

The Bias term, B0, encodes the prior probability of each class -- the bigger the term, the more likely we expect to see a Y=1 (i.e. spam).

If we have an example of X={Mother,Work,Viagra,Mother} then we use the bias term and add the weights of each word, mutiplying each feature by its frequency if it appears more than once:

![](http://note.io/1sFKQNO)

#### Estimating Coefficients: Gradient and Derivatives:

So how do we find the weights of the coefficients that maximize the conditional likelihood?
Take derivitives and gradients and use gradient descents of beta that maximize conditional likelihood.

CS229 has a detailed explanation of this in its [notes](http://cs229.stanford.edu/notes/cs229-notes1.pdf)

Here's an excerpt (but read the link above for full details):

![](http://note.io/1sFRUdm)

For our purposes, just consider that **higher weights mean that the feature is more important for a specific class.**

#### Example
Another motivating example from [mathematicalmonk's great video](https://www.youtube.com/watch?v=-Z2a_mzl9LM)

![](http://note.io/1sFNrHq)

shows that the feature fector includes the weights of each feature that may lead to death by cholestoral.  

We need to pass the equation through a sigmoid function to keep it between 0 and 1:

![](http://note.io/1sFO6bP)

We use the standard logistic function here.





### Details on the logistic Function:

* An exponential function makes big things small, a logarithmic function makes small things big
* The logistic function is just one over 1+ the exponential function.
* It looks like an S and allows us to keep the answer always between a 0 and a 1:
![](http://note.io/1sFG4jm)






### Resources
Jordan Boyd-Graber's Slides and Lecture:

http://www.umiacs.umd.edu/~jbg/teaching/DATA_DIGGING/lecture_05.pdf
Pages 17 to 32

A 15 minute Kahn-style video from MathematicalMonk:
https://www.youtube.com/watch?v=-Z2a_mzl9LM








