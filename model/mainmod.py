import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Load the dataset
dataset = pd.read_csv('model/generated_dataset.csv')
# dataset['Distance'] = dataset['Distance'] // 10
# dataset['Quantity'] = dataset['Quantity'] // 10

# print(dataset['Distance'].value_counts())
# print(dataset['Quantity'].value_counts())

# Split the data into features (X) and the target variable (y)
X = dataset[['Rating', 'Distance', 'Quantity']]
y = dataset['category']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.08, random_state=1)

# Create a Random Forest Regressor model
rf_regressor = RandomForestClassifier(n_estimators=3, max_depth=4, random_state=1)

# Train the model on the training data
rf_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_regressor.predict(X_test)



# accuracy = accuracy_score(y_test, y_pred)

# # Calculate precision, recall, and F1-score
# precision = precision_score(y_test, y_pred, average='weighted')
# recall = recall_score(y_test, y_pred, average='weighted')
# f1 = f1_score(y_test, y_pred, average='weighted')

# # Display the confusion matrix
# conf_matrix = confusion_matrix(y_test, y_pred)

# # Display a classification report
# class_report = classification_report(y_test, y_pred)

# print(f'Accuracy: {accuracy:.2f}')
# print(f'Precision: {precision:.2f}')
# print(f'Recall: {recall:.2f}')
# print(f'F1-Score: {f1:.2f}')
# print('Confusion Matrix:\n', conf_matrix)
# print('Classification Report:\n', class_report)

# for i, tree in enumerate(rf_regressor.estimators_):
#     plt.figure(figsize=(20, 10))
#     plot_tree(tree, filled=True, feature_names=X.columns, rounded=True)
#     plt.title(f'Tree {i + 1}')
#     plt.show()

sample=[[2,91,1]]

print(f"output for {sample} will be {rf_regressor.predict(sample)}")


