# Practice Goals
* Build our numpy and PANDAS repitoire: array, matrix, dataframes
* Compare the work from last week with these libraries

## Confirm our theory one more time!

    from numpy import array, dot
    from scipy import linalg
    X = array([[1, 1], [1, 2], [1, 3], [1, 4]])
    y = array([[1], [2], [3], [4]]])
    n = inv(dot(X.T, X))
    k = dot(X.T, y)
    coef_ = dot(n, k) 

And a nice short and sweet regression function with no accounting for error:

    def regression(input, response):
        return dot(linalg.inv(dot(X.T, X)), dot(X.T, y))

## Practice: NumPy

Last class we spent a huge portion of our lab time working on some basic linear algebra functions. Thankfully, NumPy and SciPy offer a lot of this already for us and more.

    from numpy import *
    arrayOne = arange(15).reshape(3, 5)
    arrayTwo = arange(15).reshape(5, 3)
    vector = array([10, 15, 20])
	print(arrayOne)
	print(arrayTwo)
	print(vector)

numpy as a standard uses arrays, which can be of any n-dimensions, though numpy has a specific subclass of arrays called matrices.

	matrixOne = matrix('1 2 3; 4 5 6')
	matrixTwo = matrix('1 2; 3 4; 5 6')
	
Bare in mind that these are still two different structures, and therefore interact differently in Python. For example: which of these produces the answer we'd expect from last class? What does the other one actually do?

    a1 = array([ [1, 2], [3, 4] ])
    a2 = array([ [1, 3], [2, 4] ])
	m1 = matrix('1 2; 3 4')
	m2 = matrix('1 3; 2 4')
	a1 * a2
	m1 * m2


Note that we can easily get around this issue using the _dot_ function:

	dot(a1, a2)
	dot(m1, m2)

That said, here's some other common functions that we built last week that are likely much more efficient as their numpy functions:

	# .T Transposes the array or matrix:
	a1.T
	# .I returns the matrix inverse:
	m1.I
	# eye(value) creates an identity matrix:
	iFive = eye(5)

Keep track of when you are using n-dimensional arrays and when you are using matrices in numpy: this can cause a lot of headaches!

## On your own
Verify the work from last week by building the matrices you tested last week and comparing your functions to numpys. Those of you more experience with Python, feel free to check speed with _timeit_:

    t.timeit('dot(a1, a2)', setup="from __main__ import dot, a1, a2", number = 100000)


## Last word on numpy
Numpy also has a lot of basic math functions built in which do not exist in python (but are common in stats languages). Feel free to go through these on your own:

	exp(10) # e ^ value
	log(1)
	sqrt(4)
	

### Practice: PANDAS

Let's use the NYTimes dataset to go through some basic functions in PANDAS.

	import pandas as pd
	df = pd.read_csv('nytimes1.csv')
	df
	df.describe()
	df[:10]

	# Create the average impressions and clicks for each age.
	dfg = df[ ['Age', 'Impressions', 'Clicks'] ].groupby(['Age']).agg([numpy.mean])
	dfg[:10]

 Likewise, we can create new variables:

	df['log_impressions'] = df['Impressions'].apply(numpy.log)

Or even recluster our values into more specific age groups:

	# Function that groups users by age.
	def map_age_category(x):
		if x < 18:
			return '1'
		elif x < 25:
			return '2'
		elif x < 32:
			return '3'
		elif x < 45:
			return '4'
		else:
			return '5'

	df['age_categories'] = df['Age'].apply(map_age_category)

    
## Classwork
The NYTimes data is hosted across 30 csv files:
    
    # Replace # with anything between 1 and 30
    http://stat.columbia.edu/~rachel/datasets/nyt1.csv
    
We'd like to use Pandas and numpy to have a simple script that aggregates all of this data into one dataframe. This time, let's just get the click through rate per age, gender, and signed_in (remember that CTR is calculated as clicks/impressions).

You can export the final dataframe using pandas to_csv:

	final_df.to_csv('nytimes_aggregation.csv')
	
Keep the csv file on your computer, but send your code over to Schoology. This should be much simpler than anything else we've done so far!

You may have to use the _astype_ function to help convert between ints and floats. Refer the to numpy documentation for more.

## Homework

Please finish your classwork if you have not.