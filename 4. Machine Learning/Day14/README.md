* Apriori is a common one in data mining. It's used to identify the most frequently occurring elements and meaningful associations in a dataset. 
* Apriori algorithm is an unsupervised algorithm that helps in creating association rules from a given dataset and the default popularity of any product. 
* Apriori utilizes three key metrics to identify interesting relationships within a dataset:
    1. Support - indicates how popular a particular itemset (a group of items) is within the dataset. It's calculated as the frequency of the itemset appearing in transactions divided by the total number of transactions. 
    2. Confidence - goes beyond just how often items appear together. It tells you the likelihood of finding item B in a transaction, given that item A is already present. It tells you the likelihood of finding item B in a transaction, given that item A is already present.
    3. Lift - goes a step further than confidence by considering the baseline likelihood of items appearing together by chance. It compares the observed confidence to the expected confidence if items were independent.
* breakdown of the steps for Apriori analysis in Python:
    1. Import Libraries
    2. Load and Explore Data
    3. Data cleaning
    3. Data Preprocessing (Optional)
    4. Define Minimum Support and Confidence
    5. Apply Apriori Algorithm
    6. Analyze Results
    7. Visualize Results (optional)

* Encoding categorical variables is a vital step in preparing data for machine learning tasks. When dealing with categorical data, characterized by non-numeric values such as text or categories, it becomes necessary to transform them into a numerical format for compatibility with machine learning algorithms.
    1. One-Hot Encoding: It creates a new binary column for each unique category in the original column. Each row of the new DataFrame will have a 1 in the corresponding category column if the item was present in the basket, and 0 otherwise. 
    2. Frequency Encoding: This assigns a numerical value to each category based on its frequency in the dataset. 
    3. Target Encoding: This is a more advanced technique where the encoding for a category is based on the average value of the target variable (e.g., purchase amount) for transactions containing that category. 