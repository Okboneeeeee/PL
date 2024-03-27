import json
import matplotlib.pyplot as plt

with open('MBTI.json', 'r', encoding="UTF-8") as jsonFile:
    data = json.load(jsonFile)

trait_expression_data = data['Trait expression']

categories = list(trait_expression_data.keys())
frequencies = list(trait_expression_data.values())

plt.figure(figsize=(10, 6))
plt.bar(categories, frequencies, color='skyblue')
plt.title('Association Between Trait Expression and Income')
plt.xlabel('Trait Expression')
plt.ylabel('Income')
##plt.xticks(rotation=45, ha='right')  

for i, v in enumerate(frequencies):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

plt.tight_layout()

plt.show()



