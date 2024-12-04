import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

# Read the data from the TSV file
df = pd.read_csv('Trypanosome_Figure_S5.tsv', sep='\t', usecols=['Sample_size_TrypOnly',
                                                                 'Richness_TrypOnly',
                                                                 'Sample_size_TrypBlood_1',
                                                                 'Richness_TrypBlood_1',
                                                                 'Sample_size_TrypBlood_Control',
                                                                 'Richness_TrypBlood_Control',
                                                                 'Sample_size_TrypBlood_2',
                                                                 'Richness_TrypBlood_2',
                                                                 'Sample_size_Feces_Control',
                                                                 'Richness_Feces_Control',
                                                                 'Sample_size_Feces_Infected',
                                                                 'Richness_Feces_Infected'])

# Create data dictionaries
Tryp_only = {'Sample Size': df['Sample_size_TrypOnly'].tolist(),
             'Richness': df['Richness_TrypOnly'].tolist()}
TrypBlood_1 = {'Sample Size': df['Sample_size_TrypBlood_1'].tolist(),
               'Richness': df['Richness_TrypBlood_1'].tolist()}
TrypBlood_Control = {'Sample Size': df['Sample_size_TrypBlood_Control'].tolist(),
                     'Richness': df['Richness_TrypBlood_Control'].tolist()}
TrypBlood_2 = {'Sample Size': df['Sample_size_TrypBlood_2'].tolist(),
               'Richness': df['Richness_TrypBlood_2'].tolist()}
Feces_Control = {'Sample Size': df['Sample_size_Feces_Control'].tolist(),
                 'Richness': df['Richness_Feces_Control'].tolist()}
Feces_Infected = {'Sample Size': df['Sample_size_Feces_Infected'].tolist(),
                  'Richness': df['Richness_Feces_Infected'].tolist()}

# Create a figure and axis for plotting
plt.figure(figsize=(10, 6))

# Plot the lines for each group
plt.plot(Tryp_only['Sample Size'], Tryp_only['Richness'], label='TrypOnly', color='tab:blue')
plt.plot(TrypBlood_1['Sample Size'], TrypBlood_1['Richness'], label='TrypBlood_1', color='tab:orange')
plt.plot(TrypBlood_Control['Sample Size'], TrypBlood_Control['Richness'], label='TrypBlood_Control', color='tab:green')
plt.plot(TrypBlood_2['Sample Size'], TrypBlood_2['Richness'], label='TrypBlood_2', color='tab:red')
plt.plot(Feces_Control['Sample Size'], Feces_Control['Richness'], label='Feces_Control', color='tab:purple')
plt.plot(Feces_Infected['Sample Size'], Feces_Infected['Richness'], label='Feces_Infected', color='tab:brown')

# Add labels and title
plt.xlabel('Sample Size')
plt.ylabel('Richness')
plt.title('Richness vs. Sample Size for Different Groups')

# Set the x-axis to scientific notation for all ticks
plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter())
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1e}'))

# Add a legend to the plot
plt.legend()

# Display the plot
plt.tight_layout()
plt.grid(True)
plt.show()

