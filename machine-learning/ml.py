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