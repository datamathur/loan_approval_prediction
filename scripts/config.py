import os

# Path to project folder.
MASTER_PATH = os.getcwd()

# Path to project sub-folders.
DATA_PATH = os.path.join(MASTER_PATH, "data")
RESULT_PATH = os.path.join(MASTER_PATH, "data")

# Path to data files.
TRAIN_DATA_PATH = os.path.join(DATA_PATH, "train.csv")
TEST_DATA_PATH = os.path.join(DATA_PATH, "test.csv")

# Information about columns in data.
TARGET_VARIABLE = ["loan_status"]
NUMERICAL_DATA_COLS = ["person_age", "person_income", "person_emp_length", "loan_amnt", "loan_int_rate", "cb_person_cred_hist_length"]
CATEGORICAL_DATA_COLS = ["person_home_ownership", "loan_intent", "loan_grade", "cb_person_default_on_file"]
ID_COLS = ["id"]