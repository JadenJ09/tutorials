
###  Feature Engineering: the process of using domain knowledge to extract features from raw data via data mining techniques
#### 1. Data Transformation: converting data into a more useful format
# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
housing_data = pd.read_csv('housing_data.csv')
X = housing_data[['Sq ft', 'Burglaries']]
y = housing_data['Rent']

# Create the model
reg = LinearRegression()

# Train the model
reg.fit(X, y)

square_footage = 1250
number_of_burglaries = 2

y_pred = reg.predict(np.array([square_footage, number_of_burglaries]).reshape(1, 2))

print(y_pred)


# %%
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Load the data
photo_id_times = pd.read_csv('photo_id_times.csv')

# Separate the data into independent and dependent variables
X = np.array(photo_id_times['Time to id photo']).reshape(-1, 1)
y = photo_id_times['Class']

# Create a model and fit it to the data
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

time_to_identify_picture = 5

# Make a prediction based on how long it takes to identify a picture
y_pred = neigh.predict(np.array(time_to_identify_picture).reshape(1, -1))

if y_pred == 1:
    print("We think you're a robot.")
else:
    print("Welcome, human!")


# %%
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import codecademylib3
from plot import plot_clusters

# Load the data
media_usage = pd.read_csv('media_usage.csv')

# Create the model
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
kmeans.fit(media_usage)

labels = kmeans.predict(media_usage)

# Plot the clusters
plot_clusters(media_usage, labels)


# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')

coffee.info()

ages = coffee['age']

min_age = np.min(ages)
print(min_age)

max_age = np.max(ages)
print(max_age)

print(max_age - min_age)

mean_age = np.mean(ages)
print(mean_age)

centered_ages = ages - mean_age
print(centered_ages)

#visualize your new list
plt.hist(centered_ages)

#label our visual
plt.title('Starbucks Customer Age Data Centered')
plt.xlabel('Distance from Mean')
plt.ylabel('Count')
plt.show()


#  %%

import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

## add code below
## set up your variables
mean_age = np.mean(ages)
print(mean_age)

## standardize ages
std_dev_age = np.std(ages)
print(std_dev_age)

## print the results 
ages_standardized = (ages - mean_age) / std_dev_age
print(ages_standardized)

print(type(ages_standardized))
print(np.mean(ages_standardized))
print(np.std(ages_standardized))


# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

## add code below
scaler = StandardScaler()

ages_reshaped = np.array(ages).reshape(-1, 1)

ages_scaled = scaler.fit_transform(ages_reshaped)

print(np.mean(ages_scaled))
print(np.std(ages_scaled))


## Same as the above
ages_fit = scaler.fit(ages_reshaped)
print(ages_fit)

ages_tr = scaler.transform(ages_reshaped)
print(ages_tr)
print(np.mean(ages_tr))
print(np.std(ages_tr))


# %%
### Min-Max Normalization

import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')
coffee.info()
## add code below
## get spent feature
spent = coffee['spent']

#find the max spent
max_spent = np.max(spent)
print(max_spent)

#find the min spent
min_spent = np.min(spent)
print(min_spent)

#find the difference
spent_range = max_spent - min_spent

#normalize your spent feature
spent_normalized = (spent - min_spent) / (max_spent - min_spent)

#print your results
print(spent_normalized)


# %%
### Min-Max Normalization with Sklearn

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

coffee = pd.read_csv('starbucks_customers.csv')
spent = coffee['spent']

## write your code below
mmscaler = MinMaxScaler()

spent_reshaped = np.array(spent).reshape(-1, 1)

reshaped_scaled = mmscaler.fit_transform(spent_reshaped)

print(np.max(reshaped_scaled))
print(np.min(reshaped_scaled))
print(set(np.unique(reshaped_scaled)))
print(np.unique(reshaped_scaled))


# %%
### Binning our Data: the process of taking numerical or categorical data and breaking it up into groups
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

print(np.min(ages))
print(np.max(ages))

age_bins = [12, 20, 30, 40, 71]

coffee['binned_ages'] = pd.cut(coffee['age'], age_bins, right = False)

print(coffee['binned_ages'].head(10))

coffee['binned_ages'].value_counts().plot(kind = 'bar')
plt.show()


#%%
### Natural Log Transformation

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn 

## add code below
## read in csv file
cars = pd.read_csv('cars.csv')
cars.info()

## set you price variable
prices = cars['sellingprice']

## plot a histogram of prices
plt.hist(prices, bins = 150)
plt.show()

## log transform prices
log_prices = np.log(prices)

## plot a histogram of log_prices
plt.hist(log_prices, bins = 150)
plt.show()


# %%
###  Ordinal  Encoding

# create dictionary of label:values in order
rating_dict = {'Excellent':5, 'New':4, 'Like New':3, 'Good':2, 'Fair':1}

#create a new column 
cars['condition_rating'] = cars['condition'].map(rating_dict)

## or
# using scikit-learn
from sklearn.preprocessing import OrdinalEncoder

# create encoder and set category order
encoder = OrdinalEncoder(categories=[['Excellent', 'New', 'Like New', 'Good', 'Fair']])

# reshape our feature
condition_reshaped = cars['condition'].values.reshape(-1,1)

# create new variable with assigned numbers
cars['condition_rating'] = encoder.fit_transform(condition_reshaped)


# %%
### Label Encoding
import pandas as pd
cars = pd.read_csv('cars.csv')

# convert 'make' feature to category type
cars['make'] = cars['make'].astype('category')
print(cars['make'].head(5))

# save new version of category codes
cars['make'] = cars['make'].cat.codes

# print to see transformation
print(cars['make'].value_counts().head(5))

# or
from sklearn.preprocessing import LabelEncoder

# create encoder
encoder = LabelEncoder()

# create new variable with assigned numbers
cars['color'] = encoder.fit_transform(cars['color'])


# %%
### One-Hot Encoding
import pandas as pd
cars = pd.read_csv('cars.csv')

## one hot encode the feature
## label this variable ohe
ohe = pd.get_dummies(cars['body'])

## print the column names
print(ohe)

## check out one of your new columns
## print the 'suv' column
print(ohe['suv'])

# %%
### Binary encoding
from category_encoders import BinaryEncoder

#this will create a new data frame with the color column removed and replaced with our 5 new binary feature columns
colors = BinaryEncoder(cols = ['color'], drop_invariant = True).fit_transform(cars)

# %%
### Hashing Encoding: a method of encoding categorical data that uses a hash function to transform the data into a hash value
### It is similar to one-hot encoding where it will create new binary columns, but within the parameters, you can decide how many features to output.   

from category_encoders import HashingEncoder

# instantiate our encoder
encoder = HashingEncoder(cols='color', n_components=5)

# do a fit transform on our color column and set to a new variable
hash_results = encoder.fit_transform(cars['color'])

# %%
### Target Encoding: a method of encoding categorical data that uses the mean of the target variable for each category
### It is similar to label encoding, but it uses the target variable to create the encoding.

from category_encoders import TargetEncoder

# instantiate our encoder
encoder = TargetEncoder(cols = 'color')

# set the results of our fit_transform to a variable 
# the output will be its own pandas series
encoder_results = encoder.fit_transform(cars['color'], cars['sellingprice'])

print(encoder_results.head())
#   color
# 0 11761.881473
# 1 18007.276995
# 2 8458.251232
# 3 14769.292595
# 4 12691.099747

# %%
### Date-Time Encoding
print(cars['saledate'].dtypes)
# # OUTPUT
# dtype('O')

cars['saledate'] = pd.to_datetime(cars['saledate'])
# #OUTPUT
# datetime64[ns, tzlocal()]

# create new variable for month
cars['month'] = cars['saledate'].dt.month

# create new variable for day of the week
cars['dayofweek'] = cars['saledate'].dt.day

# create new variable for difference between cars model year and year sold
cars['yearbuild_sold'] = cars['saledate'].dt.year - cars['year']


# %%
### Supervised Learning: a type of machine learning where the model is trained on a labeled dataset
#### 1. Regression: a type of supervised learning where the model predicts a continuous value
import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 11.5
#intercept:
b = 40

plt.plot(months, revenue, "o")

plt.show()

y = [m * month + b for month in months]

plt.plot(months, y, 'o')

plt.show()

# %%
#Loss
x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [m1*el + b1 for el in x]
y_predicted2 = [m2*el + b2 for el in x]

total_loss1 = 0

for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i]) ** 2

total_loss2 = 0

for i in range(len(y)):
  total_loss2 += (y[i] - y_predicted2[i]) ** 2

print(total_loss1)
print(total_loss2)

better_fit = lambda x, y: 1 if x < y else 2
print(better_fit(total_loss1, total_loss2))

better_fit = 2

# %%
import matplotlib.pyplot as plt
# Gradient Descent for Intercept
# -\frac{2}{N} \sum_{i=1}^{N} (y_i - (m x_i + b))
def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += (y_val - ((m * x_val) + b))
    b_gradient = -2/N * diff
    return b_gradient

# Gradient Descent for Slope
# -\frac{2}{N} \sum_{i=1}^{N} x_i(y_i - (m x_i + b))
def get_gradient_at_m(x, y, m, b):
  diff = 0
  N = len(x)
  for i in range(0, len(x)):
    y_val = y[i]
    x_val = x[i]
    diff += x_val * (y_val - (m * x_val + b))
  m_gradient = -2/N * diff
  return m_gradient

# Convergence: the process of finding the best fit line
# Learning Rate: a hyperparameter that controls how much to change the model in response to the estimated error each time the model weights are updated

# Step Gradient
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
# Gradient Descent
def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0
    for i in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)
    return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)

y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()

# %%
import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#Your gradient_descent function here:  
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()

# %%
import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

plt.plot(X, y, 'o')
#plot your line here:
b, m = gradient_descent(X, y, 0.0001, 1000)

y_predictions = [i * m + b for i in X]

plt.plot(X, y_predictions)
plt.show()

# %%
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

plt.plot(temperature, sales, 'o')
plt.show()

line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)

sales_predict = line_fitter.predict(temperature)

plt.plot(temperature, sales, 'o')
plt.plot(temperature, sales_predict, 'y')
plt.show()


# %%
# Multiple Linear Regression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['size_sqft','building_age_yrs']]
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

ols = LinearRegression()

ols.fit(x_train, y_train)

# Plot the figure

fig = plt.figure(1, figsize=(6, 4))
plt.clf()

elev = 43.5
azim = -110

ax = Axes3D(fig, elev=elev, azim=azim)

ax.scatter(x_train[['size_sqft']], x_train[['building_age_yrs']], y_train, c='k', marker='+')

ax.plot_surface(np.array([[0, 0], [4500, 4500]]), np.array([[0, 140], [0, 140]]), ols.predict(np.array([[0, 0, 4500, 4500], [0, 140, 0, 140]]).T).reshape((2, 2)), alpha=.7)

ax.set_xlabel('Size (ft$^2$)')
ax.set_ylabel('Building Age (Years)')
ax.set_zlabel('Rent ($)')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

# Add the code below:
plt.show()

# %%
#### 2. Classification: a type of supervised learning where the model predicts a category or class



### Feature Engineering: the process of using domain knowledge to extract features from raw data via data mining techniques
#### 2. Feature Selection: the process of selecting a subset of relevant features for use in model construction
#### 3. Feature Scaling: the process of standardizing the range of independent variables or features of data

### Unsupervised Learning: a type of machine learning where the model is trained on an unlabeled dataset
#### 1. Clustering: a type of unsupervised learning where the model groups similar data points together
#### 2. Dimensionality Reduction: a type of unsupervised learning where the model reduces the number of features in the dataset
