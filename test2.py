import pandas as pd

data = {
    'Age': [39, 50, 38, 53, 28, 27, 40, 58, 22, 52],
    'Workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private', 'Private', 'Private', 'Private', 'Private', 'Self-emp-inc'],
    'Income': [77516, 83311, 215646, 234721, 338409, 257302, 154374, 151910, 201490, 287927],
    'Education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors', 'Assoc-acdm', 'HS-grad', 'HS-grad', 'HS-grad', 'HS-grad'],
    'Education-Num': [13, 13, 9, 7, 13, 12, 9, 9, 9, 9],
    'Sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Capital Gain': [2174, 0, 0, 0, 0, 0, 0, 0, 0, 15024],
    'Capital Loss': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Hours per Week': [40, 13, 40, 40, 40, 38, 40, 40, 20, 40],
    'Native Country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba', 'United-States', 'United-States', 'United-States', 'United-States', 'United-States']
}

df = pd.DataFrame(data)
import numpy as np

income = df['Income']

mean_income = np.mean(income)
std_income = np.std(income)
median_income = np.median(income)

print("平均薪資：", mean_income)
print("薪資標準差：", std_income)
print("薪資中位數：", median_income)