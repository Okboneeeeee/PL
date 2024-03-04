import pandas as pd
import matplotlib.pyplot as plt

# 讀取數據
df = pd.read_csv('C:/Users/bonni/Desktop/vscode/程式語言/W1/adult.csv')

# 擷取第三列
third_column = df.iloc[:, 2]  # 行索引為所有行，列索引為 2 的列

# 選擇範圍在 70000 到 350000 之間的數據
filtered_data = third_column[(third_column >= 0) & (third_column <= 500000)]

# 製作直方圖
plt.hist(filtered_data, bins=20, range=(0, 500000), color='skyblue', edgecolor='black')

# 設置 X 軸範圍和標籤
plt.xticks(range(0, 500001, 40000), rotation=45)  # 將 X 軸的刻度設置為 70000 到 350000，間隔為 20000，並將刻度旋轉 45 度

# 添加標籤和標題
plt.title('Histogram of Third Column')
plt.xlabel('Income')
plt.ylabel('Number of People')

# 顯示圖形
plt.show()
