import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to read data from CSV files
def read_data(file_path):
    return pd.read_csv(file_path)

# Read data from CSV files
df_blood_control = read_data('TrypanosomeBlood_Control-counts-species.csv')
df_blood_infected = read_data('TrypanosomeBlood2-counts-species.csv')
df_feces_control = read_data('Feces_Control-counts-species.csv')
df_feces_infected = read_data('Feces_Infected-counts-species.csv')

# Combine data into a single DataFrame
df_blood_control['Group'] = 'TrypBlood_Control'
df_blood_infected['Group'] = 'TrypBlood_2'
df_feces_control['Group'] = 'Feces_Control'
df_feces_infected['Group'] = 'Feces_Infected'

df_combined = pd.concat([df_blood_control, df_blood_infected, df_feces_control, df_feces_infected])

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Group', y='fastq', data=df_combined, palette='Set2', inner=None, linewidth=1.25)

# Set y-axis limit
plt.ylim(0, 20000)

# Adding labels
plt.xlabel('')
plt.ylabel('Read count per classified species')
# plt.title('Violin Plot of Fastq Values by Sample Type')

# Display the plot
plt.show()
