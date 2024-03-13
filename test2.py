import pandas as pd
df = pd.read_csv('C:/Users/bonni/Desktop/vscode/程式語言/W1/adult.csv')

import numpy as np

income = df['Income']

mean_income = np.mean(income)
std_income = np.std(income)
median_income = np.median(income)

print("平均薪資：", mean_income)
print("薪資標準差：", std_income)
print("薪資中位數：", median_income)
