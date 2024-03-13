import pandas as pd


df = pd.read_csv('C:/Users/bonni/Desktop/vscode/程式語言/W3/company.csv')

name_set = set(df['Name'])
gender_set = set(df['Gender'])
education_set = set(df['Education'])


union_set = name_set.union(gender_set).union(education_set)


intersection_set = name_set.intersection(gender_set).intersection(education_set)


difference_set = name_set.difference(gender_set).difference(education_set)

print("姓名集合:", name_set)
print("性別集合:", gender_set)
print("學歷集合:", education_set)
print("聯集:", union_set)
print("交集:", intersection_set)
print("差集:", difference_set)
