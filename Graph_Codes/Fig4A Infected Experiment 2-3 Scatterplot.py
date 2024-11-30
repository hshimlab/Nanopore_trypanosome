import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import linregress

# Read the fastq columns from CSV files
df1 = pd.read_csv('Feces_Infected-counts-species.csv', usecols=['fastq'])
df2 = pd.read_csv('TrypanosomeBlood2-counts-species.csv', usecols=['fastq'])

# Ensure both dataframes have the same length
min_length = min(len(df1), len(df2))
df1 = df1.iloc[:min_length]
df2 = df2.iloc[:min_length]

# Combine the data into one DataFrame
df = pd.DataFrame({
    'x': df1['fastq'],
    'y': df2['fastq']
})

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(df['x'], df['y'])

r_squared = r_value ** 2

# Generate regression equation
p_str = f'p = {p_value:.2e}'

reg_eqn = f'Y = {slope:.2f} * X + {intercept:.2f}\nR² = {r_squared:.2f}, {p_str}'

# Color for Graph
custom_color = (69/255, 117/255, 180/255)

# Create a scatterplot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='x', y='y', scatter_kws={'s': 100, 'color': custom_color}, line_kws={'color': custom_color}, ci=95)
plt.annotate(reg_eqn, xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12, ha='center')

# Customize the plot
#plt.title('')
plt.xlabel('Read count per species of Feces_Infected')
plt.ylabel('Read count per species of TrypBlood_2')
plt.grid(False)

# Show the plot
plt.show()