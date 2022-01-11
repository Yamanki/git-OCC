import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import pandas as pd
import pickle

# Load data
houses = pd.read_csv("Housing.csv")

Y = houses['price']
X = houses['lotsize']

X = X.values.reshape(len(X), 1)
Y = Y.values.reshape(len(Y), 1)

# Split the data into training and testing sets
X_train = X[:-250]
X_test = X[-250:]

# Split the targets into training an testing sets
Y_train = Y[:-250]
Y_test = Y[-250:]

# Plot outputs
plt.scatter(X_test, Y_test)
plt.title('Test Data')
plt.xlabel('Size')
plt.ylabel('Price')
plt.xticks(())
plt.yticks(())

# Create linear regression object
model = linear_model.LinearRegression()

# Train the model using the training sets
model.fit(X_train, Y_train)

# save the model to disk
filename = 'linear_regression_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Plot outputs
plt.plot(X_test, model.predict(X_test), color='red', linewidth=3)
plt.show()
Y_pred = model.predict(np.array([500]).reshape(1, 1))
print(Y_pred)

# To use the model
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
Y_test = loaded_model.predict(np.array([700]).reshape(1, 1))
print(Y_test)
