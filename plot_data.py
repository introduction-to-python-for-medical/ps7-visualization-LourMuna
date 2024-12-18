# -*- coding: utf-8 -*-
"""plot_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/yotam-biu/tutorial7/blob/main/plot_data.ipynb
"""

# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

"""# Step 1: Select a Dataset

Choose a dataset from `sklearn`. You can use datasets such as the Iris dataset, Boston housing dataset, or any other dataset available in `sklearn.datasets`.

### 1. Iris Dataset
**Description**: A classic dataset containing measurements of 150 iris flowers from three species (Setosa, Versicolor, Virginica). Features include sepal and petal length and width.  
`fetch_openml(name='iris', version=1, as_frame=True)`

---

### 2. Wine Dataset
**Description**: Chemical analysis results for 178 wines from three cultivars. Features include alcohol content, color intensity, and magnesium levels.  
`fetch_openml(name='wine', version=1, as_frame=True)`

---

### 3. Breast Cancer Dataset
**Description**: Features derived from a digitized image of a fine needle aspirate of a breast mass. Used for binary classification (malignant or benign).  
`fetch_openml(name='breast_cancer', version=1, as_frame=True)`

---

### 4. Diabetes Dataset
**Description**: Contains 10 baseline variables for 442 diabetes patients. The target is a quantitative measure of disease progression one year after baseline.  
`fetch_openml(name='diabetes', version=1, as_frame=True)`

---

### 5. Boston Housing Dataset (Deprecated)
**Description**: Features related to housing in Boston, such as crime rate, property tax, and age of homes, with median home prices as the target.  
`fetch_openml(name='boston', version=1, as_frame=True)`

---

### 6. California Housing Dataset
**Description**: Features related to housing in California, including median income, average rooms, and population. Target is the median house value.  
`fetch_openml(name='california_housing', version=1, as_frame=True)`

---

### 7. Linnerud Dataset
**Description**: A small dataset of physical exercise data. Contains features related to exercise (e.g., weight lifted) and target variables related to physiological responses (e.g., pulse rate).  
`fetch_openml(name='linnerud', version=1, as_frame=True)`
"""

data = fetch_openml(name='iris', version=1, as_frame=True)

"""# Step 2: Inspect the Data

Once you have selected your dataset, use the following commands to explore the data:

- `data.DESCR`: View the description of the dataset to understand its context.
- `df.sample(5)`: Display a random sample of 5 rows from the dataset to get a sense of the data.
- `df.describe()`: Generate summary statistics for the dataset, including count, mean, standard deviation, min, and max values.
- `df.dtypes`: Check the data types of the features to ensure they are appropriate for analysis.

"""

print(data.DESCR)

df = data.frame

df.sample(5)

df.describe()

df.dtypes

"""---

# Step 3: Select 5 Features

After inspecting the dataset, choose 5 features that you find interesting and want to analyze further. You can access the list of feature names using `df.columns`.

Create a list of your selected features. For example:

```python
features = df.columns
selected_features = [features[0], features[2], features[4], features[6], features[7]]
```

Feel free to choose any 5 features based on the dataset you are working with.







"""

features = list(df.columns)
print("Available features:", features)
selected_features = [features[0], features[2], features[4]]
print("Selected features: ", selected_features)

"""# Step 4: Make Histogram Plots

For each of the selected features, create a histogram to visualize the distribution of the data. You can use `plt.hist()` or `plt.bar()` to create the plots.

Notice: The `.hist(bins=5)` function creates the histogram with 5 bins, but you can adjust this based on the dataset.


"""

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

"""# Step 5: Select One Feature and Test Correlation

Choose one of the selected features and test its correlation with other features using scatter plots. A scatter plot will help you visualize the relationship between two continuous variables and observe any patterns.

- For example, you might choose the first feature and plot it against each of the other selected features.
- Analyze the plots to identify any trends, such as a linear or non-linear relationship between the features.
- Look for clusters, outliers, or patterns that may indicate a strong correlation or lack thereof between the features.


"""

reference_feature = selected_features[0]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()

"""# Step 6: Choose a Single Correlation Plot and Save It

From the scatter plots, choose one feature pair that shows an interesting or strong relationship. This could be a pair that exhibits a clear trend, a non-linear pattern, or an unexpected result.

- Save the selected correlation plot as an image file using `plt.savefig('correlation_plot.png')`.
- Analyze the result by commenting on the correlation you observed. Discuss whether the relationship appears linear or non-linear, and if any patterns are evident. Consider the implications of the correlation for your data analysis and further exploration.

Ensure the saved image captures the key insights from the correlation analysis.

"""

reference_feature = selected_features[2]  # The reference feature
comparison_feature = selected_features[0]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()

