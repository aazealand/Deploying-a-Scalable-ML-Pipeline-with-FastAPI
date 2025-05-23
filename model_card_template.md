# Model Card

## Model Details
This project uses the [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) model from sklearn with the following parameters:
- random_state=42
- solver='liblinear'
## Intended Use
This model is for educational purposes only. It is used as a component of a machine learning deployment project.
## Training Data
This model was trained on [data](https://archive.ics.uci.edu/dataset/20/census+income) from the 1994 Census database.
## Evaluation Data
This model used 20% of the downloaded data for evaluation.
## Metrics
This model uses demographic variables (age, education, occupation, etc.) to predict whether an individual makes over $50K per year.

### Overall Model Performance:

| Precision | Recall | F1 |
| :---: | :---: | :---: |
| 0.7220 | 0.2712 | 0.3943 |

**What Does This Mean?**
* **Precision:** When our model predicts that someone has a annual salary above $50K, it is correct **72.2%** of the time.

* **Recall:** However, our model only identifies **27.1%** of people who *actually* make more than $50K a year.

* **F1:** Our model's F-score is only **0.39**. For our educational purposes, this is fine. But, if we needed to rely on these predictions it would be unsatisfactory. We would need to fine tune the selected model (logistic regression), or use a different model altogether.

### Model Performance for a Specific Slice (Education):
![Education Metrics](/screenshots/edu_slice_values.png)

**Precision:** When our model predicts that someone with `education level` has a annual salary above $50K, it is correct `%` of the time:
* Bachelors: 81%
* HS-grad: 61%
* Masters: 86%
* Some-college: 62%

**Recall:** However, our model only identifies `%` of `education level` that actually make more than $50K a year. (The results we see here are quite low.)
* Bachelors: 29%
* HS-grad: 21%
* Masters: 30%
* Some-college: 23%

**F1:** For this slice, our model's highest F-score is only 0.44. For our educational purposes, this is fine. But, if we needed to rely on these predictions it would be unsatisfactory.


## Ethical Considerations
This model should not be used to make decisions that actually affect people's lives (e.g. credit decisions). If it were, the low recall (27%) would unfairly disadvantage people who make more than $50K a year (i.e. the model would fail to identify them and they may miss out on offers of credit).

## Caveats and Recommendations
Remember, this model is for educational purposes only. It serves only as an example of an ML training pipeline with an API.