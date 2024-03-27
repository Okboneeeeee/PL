import json
import matplotlib.pyplot as plt

with open('MBTI.json', 'r', encoding="UTF-8") as jsonFile:
    data = json.load(jsonFile)

mbti_categories_data = data['MBTI categories']

categories = list(mbti_categories_data.keys())
frequencies = list(mbti_categories_data.values())

plt.figure(figsize=(10, 6))
plt.bar(categories, frequencies, color='skyblue')
plt.title('Association Between MBTI Categories and Income')
plt.xlabel('MBTI Categories')
plt.ylabel('Income')
##plt.xticks(rotation=45, ha='right')  

for i, v in enumerate(frequencies):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

plt.tight_layout()

plt.show()
