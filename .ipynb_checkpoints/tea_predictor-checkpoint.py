import numpy as np
import pandas as pd
import os
from PIL import Image

# Get all the names of the subfolders
main_path = '/Users/karlboma/Documents/Python Stuff/Side Projects/Tea Disease Classification Project/tea sickness dataset'

sub_folders = [name for name in os.listdir(main_path) if os.path.isdir(os.path.join(main_path, name))]

print(sub_folders)

# Convert all the images into a numpy array and add it to the data and targe arrays
data = []
target = []

for folder in sub_folders:
    image_path = main_path + f"/{folder}"
    for image in os.listdir(image_path):
        img = Image.open(image_path + f"/{image}")
        img_array = np.array(img).flatten()
        data.append(img_array)
        target.append(folder)

data = np.array(data)
target = np.array(target)

# Convert the string labels into numerical labels
labels_dict = {'white spot': 0,
               'Anthracnose': 1,
               'healthy': 2,
               'gray light': 3,
               'bird eye spot': 4,
               'algal leaf': 5,
               'brown blight': 6,
               'red leaf spot': 7}

target = np.vectorize(labels_dict.get)(target)

# Initialize Linear SVC model
from sklearn.svm import LinearSVC
model = LinearSVC()

# Use KFold cross validation to asses model
from sklearn.model_selection import KFold

kf = KFold(n_splits = 5)

for train_index, test_index in kf.split(data):
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = target[train_index], target[test_index]

    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the testing set
    y_pred = model.predict(X_test)
    
    # Evaluate and store the performance
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Compute overall performance
mean_accuracy = sum(accuracies) / len(accuracies)
print(f"Mean Accuracy across 5 folds: {mean_accuracy:.4f}")