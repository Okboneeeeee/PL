import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/bonni/Desktop/vscode/程式語言/W1/adult.csv')
third_column = df.iloc[:, 2]  
filtered_data = third_column[(third_column >= 0) & (third_column <= 500000)]
plt.hist(filtered_data, bins=20, range=(0, 500000), color='skyblue', edgecolor='black')
plt.xticks(range(0, 500001, 40000), rotation=45)

plt.title('Histogram of Third Column')
plt.xlabel('Income')
plt.ylabel('Number of People')

plt.show()
