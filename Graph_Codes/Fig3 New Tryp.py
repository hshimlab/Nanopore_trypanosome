import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function to read data from CSV files
def read_data(file_path):
    return pd.read_csv(file_path)

# Read data from CSV files
df_blood_control = read_data('TrypanosomeBlood_Control-counts-species.csv')
df_blood_infected = read_data('TrypanosomeBlood2-counts-species.csv')
df_feces_control = read_data('Feces_Control-counts-species.csv')
df_feces_infected = read_data('Feces_Infected-counts-species.csv')

# Calculate means and standard deviations for the 'fastq' column
control_means = [
    df_blood_control['fastq'].mean(),
    df_feces_control['fastq'].mean()
]
infected_means = [
    df_blood_infected['fastq'].mean(),
    df_feces_infected['fastq'].mean()
]
control_std = [
    df_blood_control['fastq'].std(),
    df_feces_control['fastq'].std()
]
infected_std = [
    df_blood_infected['fastq'].std(),
    df_feces_infected['fastq'].std()
]

# Categories
categories = ['Blood', 'Feces']

# Combine the means and standard deviations for each category
means = [control_means, infected_means]
stds = [control_std, infected_std]

# Bar width
bar_width = 0.35
colors = ['grey', 'white']

# X positions for the bars
index = np.arange(len(categories))

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plotting the bars for each group
labels = ['Control', 'Infected']
for i in range(len(means)):
    ax.bar(index + i * bar_width, means[i], bar_width, capsize=5, label=labels[i], color=colors[i],
           edgecolor='black', yerr=stds[i])

# Adding labels, title, and legend
ax.set_xlabel('Sample Type')
ax.set_ylabel('Average Count')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()

# Display the plot
plt.show()
