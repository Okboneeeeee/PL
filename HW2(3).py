import json
import matplotlib.pyplot as plt

# 打开并加载JSON文件
with open('MBTI.json', 'r', encoding="UTF-8") as jsonFile:
    data = json.load(jsonFile)

# 提取MBTI类别数据
Trait_expression_gender_data = data['Trait expression and gender']

# 获取类别和频率
categories = list(Trait_expression_gender_data.keys())
frequencies = list(Trait_expression_gender_data.values())

# 创建条形图
plt.figure(figsize=(10, 6))
plt.bar(categories, frequencies, color='skyblue')
plt.title('Association Between Trait Expression - Gender and Income')
plt.xlabel('Trait Expression - Gender')
plt.ylabel('Income')
plt.xticks(rotation=45, ha='right')  # 旋转x轴刻度，使标签更易读

for i, v in enumerate(frequencies):
    plt.text(i, v +0.5, str(v), ha='center', va='bottom')

plt.tight_layout()

# 显示图形
plt.show()
