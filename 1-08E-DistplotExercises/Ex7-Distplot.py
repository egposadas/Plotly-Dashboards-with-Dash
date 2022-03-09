#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')

# Define the traces
t1 = df[df['class']=='Iris-setosa']['petal_length']
t2 = df[df['class']=='Iris-versicolor']['petal_length']
t3 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
hist_data = [t1,t2,t3]
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1,.1,.1])
pyo.plot(fig, filename='ex7.html')

########
# Great! This shows that if given a flower with a petal length
# between 1-2cm, it is almost certainly an Iris Setosa!
######
