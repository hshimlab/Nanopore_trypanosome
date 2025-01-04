import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dataframes
df1 = pd.read_csv("TrypanosomeBlood_Control-counts-species.csv")
df2 = pd.read_csv("TrypanosomeBlood2-counts-species.csv")

# Filtering for Terms
filtered_strings = {'Archaea': (82/255, 82/255, 82/255),
    'Viruses': (150/255, 150/255, 150/255),
    'Eukaryota': (204/255, 204/255, 204/255),
    'Bacteria': (247/255, 247/255, 247/255)}
# Counting
count_dict1 = {}
count_dict2 = {}

for string in filtered_strings:
    count_dict1[string] = df1[df1['superkingdom'].str.contains(string)].shape[0]
    count_dict2[string] = df2[df2['superkingdom'].str.contains(string)].shape[0]

sorted_counts1 = sorted(count_dict1.values())
sorted_counts2 = sorted(count_dict2.values())

num_categories = len(filtered_strings)

# Scale of Chart
plt.figure(figsize=(4, 4))
bar_width = .8
index = np.arange(2)

# Create Chart
fig, ax = plt.subplots(figsize=(4,6))

bottom1 = [0] * len(filtered_strings)
bottom2 = [0] * len(filtered_strings)


for idx, (string, color) in enumerate(filtered_strings.items()):
    # Bar for dataset 1
    bars1 = ax.bar('TrypBlood_Control', sorted_counts1[idx], bottom=bottom1, color=color, edgecolor="black", label=string, width=bar_width)
    bottom1 = [bottom1[i] + sorted_counts1[idx] for i in range(len(bottom1))]

    # Bar for dataset 2
    bars2 = ax.bar('TrypBlood_2', sorted_counts2[idx], bottom=bottom2, color=color, edgecolor="black", width=bar_width)
    bottom2 = [bottom2[i] + sorted_counts2[idx] for i in range(len(bottom2))]

# Labeling
#ax.legend(loc='upper left')
# plt.xlabel('Experimental Samples')
plt.ylabel('Number of Species in Superkingdom')
#plt.title('Comparison Sequencing Data Between Blood Samples')
plt.xticks(rotation=45, ha='center', fontsize=8)
ax.set_ylim(0,400)
plt.tight_layout()
plt.show()
