# Exploratory Data Analysis

This dataset consists of a [`train.py`](../data/train.csv) and a [`test.py`](../data/test.csv). I will be analysing the data in `train.py` file to understand data distribution and plan model training process.

The execution notebook for EDA can be found at [EDA.ipynb](../EDA.ipynb)

The traning data can be described by the following properties:

1. The data has **13 columns** out of which 12 are used as features and 1 is used as target.
2. The data has **58645 data points** which I plan to divide into Training and Validation data using a 80-20 split.
3. **Target Distribution**:

   **No** - 50295 (85.76%)

   **Yes** - 8350 (14.24%)
4. **Features**:
   - 'id'
   - 'person_age'
   - 'person_income'
   - 'person_home_ownership'
   - 'person_emp_length'
   - 'loan_intent'
   - 'loan_grade'
   - 'loan_amnt'
   - 'loan_int_rate'
   - 'loan_percent_income'
   - 'cb_person_default_on_file'
   - 'cb_person_cred_hist_length'
     
   **Target**: 
   - 'loan_status' 

## 1D Data Analysis