import matplotlib.pyplot as plt
import pandas as pd

# Function to read data from CSV files
def read_data(file_path):
    return pd.read_csv(file_path)

# Read data from CSV files
df_blood_control = read_data('TrypanosomeBlood_Control-counts-species.csv')
df_blood_infected = read_data('TrypanosomeBlood2-counts-species.csv')
df_feces_control = read_data('Feces_Control-counts-species.csv')
df_feces_infected = read_data('Feces_Infected-counts-species.csv')

# Group data by sample type
data = {
    'Blood Control': df_blood_control['fastq'],
    'Blood Infected': df_blood_infected['fastq'],
    'Feces Control': df_feces_control['fastq'],
    'Feces Infected': df_feces_infected['fastq']
}

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create a box plot
ax.boxplot(data.values(), patch_artist=True,
           boxprops=dict(color='black'),
           medianprops=dict(color='black'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           flierprops=dict(markerfacecolor='black', marker='o', markersize=5))

# Adding labels, title, and legend
#ax.set_xlabel('Sample Type')
plt.ylim(top=100)
ax.set_ylabel('Fastq Values')
ax.set_xticklabels(data.keys())

# Display the plot
plt.show()