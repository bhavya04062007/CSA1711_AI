import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

# input training data for XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# output required for XOR
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Build the neural network model
model = Sequential()

# Hidden layer with neurons and 'tanh' activation function
model.add(Dense(input_dim=2, activation='tanh', units=8))

# Output layer with 'sigmoid' activation function
model.add(Dense(input_dim=8, activation='sigmoid', units=1))

# Compile the model using binary crossentropy
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Make prediction and evaluate the model
print("Prediction for XOR input:")
predictions = model.predict(X)
rounded_predictions = np.round(predictions)
print("Rounded Predictions")
print(rounded_predictions)
