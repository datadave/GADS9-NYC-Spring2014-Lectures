## PANDAS Practice

Load the `iris` data set from the web using this url.
`https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv`

The iris data set is well known, learn more about it <a href="http://en.wikipedia.org/wiki/Iris_flower_data_set">here</a>!

Answer the following questions using python, numpy, and pandas.

1. How many different names of flowers are in this data set?
2. How many exist of each type of flower?

3. Determine the min, median, mean, max for each numeric feature in the data set.
4. Determine the same for each flower type.
5a. How does the shape of these results change from the average of all flowers?
6b. Which features seem to be the most important in determining what kind of flower it is?

For example, you can phrase this like:
"Most Setosa Flower have a ____ petal width and a _____ sepal width."

7. Sort the data frame by each column (aside from Name), and print the results of each. What interesting trends exist in this data set, based on distributions?

**8**. write several functions to apply to the data frame that attempt to organize the data set using strings instead of floats, like our short_or_long function from lecture. Use this to best summarize your data.

**9**. CHALLENGE QUESTION: From everything above, you should be able to predict relatively accurately for each row what kind of flower it is (without using the Name column as an obvious hint). Write a function that uses the data with if and else statements to attempt to classify each row.
