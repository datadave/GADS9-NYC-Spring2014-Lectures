
#Time Series Analysis

"Prediction is very difficult, especially if it's about the future." -- Nils
Bohr

“Experience with real-world data, however, soon convinces one
that both stationarity and Gaussianity are fairy tales invented
for the amusement of undergraduates.”
--Thomson

“All models are wrong. Some models are useful” --Box



### Time Series Data
* Anything that is observed or measured at many points in time fors a time
series.
* Time series include:
    * _Timestamps_, specific instants in time
    * _Fixed periods_, i.e. the month of August 2014
    * _Intervals_, indicated by a start and end timestamp.
    * _Elapsed Time_, A measure relative to a given start time.





### Ways that Pandas Handles Time Series Data
* __Types__: date, time, datetime, timedelta
* __String Parsing__
* __Date ranges, frequencies and shifting__
* __Resampling__
* __Time Zone Awareness__
* __Plotting and Moving Window Functions__


   _source: Python for Data Analysis_

### Basic Objectives of Time Series Analysis
_([source](https://onlinecourses.science.psu.edu/stat510/?q=node/47))_

* The basic objective usually is to determine a model that describes the pattern
of the time series.  Uses for such a model are:
    * To describe the important features of the time series pattern.
    * To explain how the past affects the future or how two time series can
“interact”.
    * To forecast future values of the series.
    * To possible serve as a control standard for a variable that measures the
quality of product in some manufacturing situations.

### Types of Models, MA, AR and ARMA

There are two basic types of “time domain” models.

Models that relate the present value of a series to past values and past
prediction errors - these are called ARIMA models (for Autoregressive Integrated
Moving Average).

Ordinary regression models that use time indices as x-variables.  These can be
helpful for an initial description of the data and form the basis of several
simple forecasting methods.

###Important Characteristics to Consider First

Some important questions to first consider when first looking at a time series
are:

* Is there a trend, meaning that, on average, the measurements tend to increase
(or decrease) over time?
* Is there seasonality, meaning that there is a regularly repeating pattern of
highs and lows related to calendar time such as seasons, quarters, months, days
of the week, and so on?
* Are their outliers? In regression, outliers are far away from your line. With
time series data, your outliers are far away from your other data.
* Is there a long-run cycle or period unrelated to seasonality factors?
* Is there constant varianceover time, or is the variance non-constant?
* Are there any abrupt changes to either the level of the series or the
variance?

Statistical stationarity: A stationary time series is one whose statistical
properties such as mean, variance, autocorrelation, etc. are all constant over
time.



### Resources

| Title | Description |
| ----- | ----------- |
| [Three Hour Time Seres in Pandas Video by Wes McKinney](https://www.youtube.com/watch?v=0unf-C-pBYE) | Wes wrote Pandas.  And the book on Pandas. |
| [Time Series with Pandas](http://nbviewer.ipython.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb) | PYNB given at at a pycon |
| [Pandas Time Series Docs](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-series-date-functionality) | Extensive docswith examples on Pandas ts functionality |
| [PyData FinancialAnalysis](http://www.hilpisch.com/YH_PyData_Eurex_Tutorial.html#/8/1) | Notebookwith Eurex examples |
| [Twiecki's Financial Analysis Tutorial - GoogleTrends](http://nbviewer.ipython.org/github/twiecki/financial-analysis-python-tutorial/tree/master/) replicates google trends trading strategy in pandas, with backtest via zipline |
| [StatsModels TSA Documentation](http://statsmodels.sourceforge.net/devel/tsa.html) | Docs for the extensive sm package for use with scipy |
| [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do) |Pages 289 to 327 deal with Time Series |
| [Auto Correlation Plots Explained](http://www.itl.nist.gov/div898/handbook/eda/section3/autocopl.htm) |
| [Stat 510: Applied Time Series Analysis](https://onlinecourses.science.psu.edu/stat510/) | Overview of core concepts with examples in R in 14 lessons|
| [StatsModels Slides](http://conference.scipy.org/scipy2011/slides/mckinney_time_series.pdf) 
| [Ben Lambert's Time Series Videos](https://www.youtube.com/watch?v=v70-kLB3BLM)| Kahn Style, many topics in tsa. |
| [Financial Forecasting](http://www.quantstart.com/articles/Forecasting-Financial-Time-Series-Part-1) | Great series of articles on forecasting with Python from QuantStart |




