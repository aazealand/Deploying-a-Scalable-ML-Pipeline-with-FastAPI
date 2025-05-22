# Model Card

## Model Details
  model = LogisticRegression(random_state=42, solver='liblinear')
## Intended Use
This model is for educational purposes only.
To learn about ML deployment in pipelines
## Training Data
Model was trained on 1994 Census Data (https://)
## Evaluation Data
train, test = train_test_split(data, test_size=0.2, random_state=42)
## Metrics
model's performance
The goal was to predict wheteher a person makes over 50k a year based on other variables (age, education, occupation, etc)
Overall:
Precision: 0.7220 | Recall: 0.2712 | F1: 0.3943

#### Precision
When our model predicts that someone with [education level] has a annual salary above $50K, it is correct [percent] of the time:
* Bachelors: 81%
* HS-grad: 61%
* Masters: 86%
* Some-college: 62%

#### Recall
However, our model only identifies [percent] of [education level] that actually make more than $50K a year.
* Bachelors: 29%
* HS-grad: 21%
* Masters: 30%
* Some-college: 23%

This is quite low.

#### F1
Our model's highest F-score is only 0.44. For our purposes, we'll consider this unsatisfactory should consider fine tuning the logistic regression model we've chosen, or selecting a different model altogether.

![Education Metrics](/screenshots/edu_slice_values.png)

## Ethical Considerations
If this model were used for credit decisions or targeted marketing, it would unfairly disadvantage local government workers by missing most high earners in this category.
## Caveats and Recommendations
3. Potential Bias: The model may have learned that government workers typically earn less, causing it to systematically underpredict high earners in this sector.