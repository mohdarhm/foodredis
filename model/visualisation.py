# regression plot: wrong.

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# dataset = pd.read_csv('model\generated_dataset.csv')

# sns.lmplot(x='Rating', y='coefficient', data=dataset, ci=None)

# plt.xlabel('Ratings')
# plt.ylabel('Quantity')
# plt.title('Regression Plot: Ratings vs. Score')

# plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv('model/generated_dataset.csv')

# Create a heatmap
corr_matrix = dataset.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', linewidths=0.5)
plt.title('Correlation Heatmap')                
plt.show()
