import matplotlib.pyplot as plt
import pandas as pd

# Dataframe setup
data = {
    'Species': [
        'Duncaniella sp. B8', 'Duncaniella dubosii', 'Muribaculum intestinale',
        'Curtobacterium flaccumfaciens', 'Bacteroides caecimuris',
        'Duncaniella sp. C9', 'Homo sapiens', 'Escherichia coli',
        'Parabacteroides distasonis', 'Muribaculum gordoncarteri'
    ],
    'Count': [59976, 46633, 39362, 27265, 22941, 18600, 16493, 15952, 13010, 12531]
}

df = pd.DataFrame(data)

# Define custom order
custom_order = [
    'Escherichia coli', 'Duncaniella dubosii', 'Curtobacterium flaccumfaciens',
    'Muribaculum intestinale', 'Duncaniella sp. B8', 'Duncaniella sp. C9',
    'Homo sapiens', 'Muribaculum gordoncarteri', 'Bacteroides caecimuris',
    'Parabacteroides distasonis'
]

# Reverse the custom order
reversed_order = custom_order[::-1]

# Define custom colors
custom_colors = [
    (165/255, 0/255, 38/255), (215/255, 48/255, 39/255), (244/255, 109/255, 67/255),
    (253/255, 174/255, 97/255), (254/255, 224/255, 144/255), (224/255, 243/255, 248/255),
    (171/255, 217/255, 233/255), (116/255, 173/255, 209/255), (69/255, 117/255, 180/255),
    (49/255, 54/255, 149/255)
]

# Create a mapping of species to custom colors
species_colors = dict(zip(custom_order, custom_colors))

# Add color column based on the species_colors mapping
df['Color'] = df['Species'].map(species_colors)

# Reorder the DataFrame based on reversed custom order
df['Species'] = pd.Categorical(df['Species'], categories=reversed_order, ordered=True)
df_sorted = df.sort_values('Species')

# Plotting
plt.figure(figsize=(8, 10))

# Initialize the bottom of the stacked bars
bottom = 0

# Add stacked segments for each species
for idx, row in df_sorted.iterrows():
    plt.bar('Feces_Infected', row['Count'], bottom=bottom, color=row['Color'], edgecolor='black')
    bottom += row['Count']

# Create legend with species names and corresponding colors
legend_patches = [
    plt.Rectangle((0, 0), 1, 1, color=species_colors[species], label=species)
    for species in custom_order
]

plt.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5))

# Create Chart
plt.ylabel('Read Count per Species in Feces_Infected', fontsize=18)
plt.tight_layout()
plt.show()
