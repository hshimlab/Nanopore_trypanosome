import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dataframes
df1 = pd.read_csv("Feces_Control-counts-species.csv")
df2 = pd.read_csv('Feces_Infected-counts-species.csv')

# Filtering for Terms
filtered_strings = {'Archaea': (77/255, 172/255, 38/255),
    'Viruses': (184/255, 225/255, 134/255),
    'Eukaryota': (241/255, 182/255, 218/255),
    'Bacteria': (208/255, 28/255, 139/255)}
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
plt.figure(figsize=(4, 6))
bar_width = .3
index = np.arange(2)

# Create Chart
fig, ax = plt.subplots(figsize=(4,6))

bottom1 = [0] * len(filtered_strings)
bottom2 = [0] * len(filtered_strings)


for idx, (string, color) in enumerate(filtered_strings.items()):
    # Bar for dataset 1
    bars1 = ax.bar('Mouse Blood Control', sorted_counts1[idx], bottom=bottom1, color=color, label=string, width=bar_width)
    bottom1 = [bottom1[i] + sorted_counts1[idx] for i in range(len(bottom1))]

    # Bar for dataset 2
    bars2 = ax.bar('Trypanosome Infected Blood', sorted_counts2[idx], bottom=bottom2, color=color, width=bar_width)
    bottom2 = [bottom2[i] + sorted_counts2[idx] for i in range(len(bottom2))]

# Labeling
#ax.legend(loc='upper left')
plt.xlabel('Experimental Samples')
plt.ylabel('Number of Species in Superkingdom')
#plt.title('Comparison Sequencing Data Between Blood Samples')
plt.xticks(rotation=45, ha='center', fontsize=8)
plt.tight_layout()
plt.show()