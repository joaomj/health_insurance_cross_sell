
# Insurance Cross Sell

Using Machine Learning algorithms to optimize an insurance company's marketing campaigns.


## Business Problem
An insurance company wants to offer new auto insurance to its customers. However, its marketing budget is limited. The company asked its Data Science team to find out which customers should be given priority to receive new insurance offers.

## Business Assumptions
## Solution Strategy
After understanding the problem (optimizing the use of the marketing budget), the company's data team adopted a strategy of **classification**: customers will be classified according to the probability of purchasing the new insurance. This probability will be provided by a Machine Learning algorithm.

With the base ordered by the purchase probability, the marketing team will be able to focus its efforts only on the customers that are at the top of the sorted dataset ( = greater purchase probability).

Thus, we can say that the expected result of Machine Learning models is to group the customers most likely to purchase at the top of the dataset, so that a small % of the dataset, concentrated at the top, contains a large % of the customers most likely to purchase.

That is, in data scientists lingo, a **“Learn to Rank”** solution.
### Solution Steps
#### 1. Data Extraction
The original dataset is at Kaggle, but for educational purposes it was stored in a SQL database on AWS.

#### 2. Data Cleaning
**2.1. Data Overview:** head, dimensions, data types.

**2.2. Null Value Check**

**2.3. Checking Attribute Types**

#### 3. Exploratory Data Analysis - EDA

**3.1. Descriptive statistics**

**3.2. Separation of Attribute Classes:** numeric and categorical.

**3.3. Univariate Analysis**

**3.4. Bivariate Analysis:** relationship between the response variable and several attributes, most of them categorical.

**3.5. Multivariate analysis:**

**3.5.1. Correlation between all numeric attributes:** Pearson Correlation.

**3.5.2. Verification of the degree of relationship between categorical attributes:** Cramér's V.

#### 4. Data Preparation

**4.1. Split dataset:** into training set and test set.

**4.2. Standardization**

**4.3. Rescaling**

**4.4. Encoding**

#### 5. Features Selection: 
The ExtraTrees classifier algorithm was used to select attributes.

#### 6. Machine Learning Model Training
Four models were chosen for evaluation: K-Nearest Neighbors, Linear Regression, ExtraTrees and Random Forest.

#### 7. Machine Learning Model Selection
The trained models were evaluated through **Holdout Validation** and **Cross-validation**. 

The evaluation metrics are: *Precision@K* and *Recall@K*, the latter being the most important for the problem at hand.

#### 8. Machine Learning Model Deployment

![deploy_architecture](/health_insurance_cross-sell/references/deploy_architecture.png)

[Credits](https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42)

The model was deployed as a containerized **AWS Lambda Function** via **Docker**.

The “real” data (the test dataset) was hosted on **AWS S3**.

Access to the model is through a **Streamlit** application hosted in a virtual machine on AWS EC2: [ACCESS URL](http://3.93.153.219:8501/).

In this application, a web page asks the user to inform the percentage of customers most likely to buy that he wants to know (top %).
The application then returns a table containing the data of these customers with the option to download this table as a .csv file
## Top 3 Data Insights
### Insight 01:

![insight01](/health_insurance_cross-sell/reports/figures/insight-01-pct-responses.png)

Only 12.26% of customers are interested in a new insurance offer. Considering the size of the base (300k+ customers), it is necessary to develop a solution to find these few interested customers at a low cost.

### Insight 02:

![insight02](/health_insurance_cross-sell/reports/figures/insight02-avg-age-interested.png) 

The average age of interested customers is approximately 45 years.

### Insight 03: 

![insight03](/health_insurance_cross-sell/reports/figures/insight03-damaged-before.png)

Customers with a previously damaged vehicle are 45x more likely to wish to receive a new insurance offer.
## Machine Learning Model Applied
After cross-validation, the model chosen was Random Forest, as it presented the best average result in the *Recall@K* metric, the most relevant in this problem.

## Machine Learning Performance

**Holdout Validation:**
|Model              |Precision  |Recall |k%    |
|:-----------------:|:---------:|:-----:|:----:|
|random_forest      |0.2718     |0.8921 |40.0  |
|extra_trees        |0.2696     |0.8848 |40.0  |
|linear_regression  |0.2659     |0.8726 |40.0  |
|knn                |0.2616     |0.8587 |40.0  |

**Cross-validation:**
|Model              |k_folds    |precision_avg  |precision_std  |recall_avg     |recall_std |k%    |
|:-----------------:|:---------:|:-------------:|:-------------:|:-------------:|:---------:|:----:|
|random_forest      |5          |0.2734         |0.0007         |0.8924         |0.0020     |40.0  |
|extra_trees        |5          |0.2697         |0.0009         |0.8800         |0.0019     |40.0  |
|linear_regression  |5          |0.2672         |0.0016         |0.8720         |0.0029     |40.0  |
|knn                |5          |0.2631         |0.0008         |0.8587         |0.0016     |40.0  |

## Business Results
With the Machine Learning model adopted, the marketing team made call campaigns for ~90% of interested customers, reaching only 40% of the total customer base.

Assuming a cost per call of [$10.00](https://insuranceleadsguide.com/buying-insurance-leads/) and considering the total number of customers (381,109), the company achieved savings of $2,286,660 on phone calls costs (60% cost reduction).
## Next Steps
* Implement access control to the application link.
* Allow user to upload customer data as a csv file.
* Display a dashboard on the application page with a brief exploratory analysis of the customer dataset used.
* Implement versioning of databases and ML models.
## Conclusion
In this project, it was demonstrated how the data scientists team can optimize a company's marketing budget allocating it to the people most likely to buy.

The [CRISP-DM framework, adapted for Data Science](https://towardsdatascience.com/crisp-dm-ready-for-machine-learning-projects-2aad9172056a) was used to organize the resolution of this problem. The main reason for adopting this framework is its ability to offer solutions and business insights quickly, on an ongoing basis, during a Data Science project.

Finally, in this project I had the opportunity to use solutions from the largest cloud provider in the world (AWS) to make the resolution of this problem as close as possible to a real situation.
## References
* Kaggle Dataset: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction
* CRISP-DM for Data Scientists: https://towardsdatascience.com/crisp-dm-ready-for-machine-learning-projects-2aad9172056a
* Cost per Lead in the Insurance Market: https://insuranceleadsguide.com/buying-insurance-leads/
* Cramér's V correlation matrix: https://www.kaggle.com/code/chrisbss1/cramer-s-v-correlation-matrix/notebook
* Hold-out vs. Cross-validation in Machine Learning: https://medium.com/@eijaz/holdout-vs-cross-validation-in-machine-learning-7637112d3f8f
* Precision and Recall at K: https://medium.com/@m_n_malaeb/
recall-and-precision-at-k-for-recommender-systems-618483226c54
* Serverless Deployment of Machine Learning Models on AWS Lambda: https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42
* Deploying a Streamlit app on AWS EC2: https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3
* Fundamentals of MLOps — Part 2 | Data & Model Management with DVC: https://medium.com/analytics-vidhya/fundamentals-of-mlops-part-2-data-model-management-with-dvc-6be2ad284ec4
