import pandas as pd
import numpy as np

# Create an empty DataFrame
dataset = pd.DataFrame(columns=['NGO_ID', 'Restaurant_ID', 'Rating', 'Distance', 'Quantity', 'Category'])

# Number of data points
n = 15000

# Define the preference distribution
preference_weights = [0.5, 0.3, 0.2]

data_rows=[]

for _ in range(n):

    # Generate random data for the features
    rating = np.random.choice([i for i in range(1,6)], p=[0.2 for _ in range(5)])
    distance = np.random.randint(1,100)
    quantity = np.random.randint(1, 50)

    # Calculate the score based on the chosen legend
    if rating == 1:
        category = np.random.choice([1, 2, 3, 4, 5], p=[0.7, 0.1, 0.1, 0.05, 0.05])
    elif rating == 2:
        category = np.random.choice([1, 2, 3, 4, 5], p=[0.05, 0.35, 0.25, 0.15, 0.2])
    elif rating == 3:
        category = np.random.choice([1, 2, 3, 4, 5], p=[0.05, 0.1, 0.4, 0.2, 0.25])
    elif rating == 4:
        category = np.random.choice([1, 2, 3, 4, 5], p=[0.05, 0.15, 0.2, 0.3, 0.3])
    else:
        category = np.random.choice([1, 2, 3, 4, 5], p=[0.025, 0.025, 0.05, 0.05, 0.85])

    # Create a new row and add it to the dataset
    new_row = {'Rating': rating, 'Distance': distance, 'Quantity': quantity, 'Category ': category}
    data_rows.append({'Rating': rating, 'Distance': distance, 'Quantity': quantity, 'category': category})

# Save the dataset to a CSV file

dataset = pd.DataFrame(data_rows)
dataset.to_csv('model\generated_dataset.csv', index=False)
