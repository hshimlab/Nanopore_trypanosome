import matplotlib.pyplot as plt
import pandas as pd

# Dataframe setup
data = {
    'Species': [
        'Escherichia coli', 'Duncaniella dubosii', 'Curtobacterium flaccumfaciens',
        'Muribaculum intestinale', 'Duncaniella sp. B8', 'Mucispirillum schaedleri',
        'Homo sapiens', 'Muribaculum gordoncarteri', 'Bacteroides caecimuris',
        'Parabacteroides distasonis'],
    'Count': [14483, 8729, 8234, 8218, 7367, 6742, 6617, 4236, 4005, 3629],
    'Color': [
        (165/255, 0/255, 38/255), (215/255, 48/255, 39/255), (244/255, 109/255, 67/255),
        (253/255, 174/255, 97/255), (254/255, 224/255, 144/255), (224/255, 243/255, 248/255),
        (171/255, 217/255, 233/255), (116/255, 173/255, 209/255), (69/255, 117/255, 180/255),
        (49/255, 54/255, 149/255)
    ]
}

df = pd.DataFrame(data)

# Sort DataFrame by 'Count' column
df_sorted = df.sort_values(by='Count', ascending=False)

# Plotting
plt.figure(figsize=(8, 10))

# Add stacked segments for each species
bottom = 0
for idx, row in df_sorted.iloc[::-1].iterrows():  # Reverse the order of rows while plotting
    plt.bar('Feces_Infected', row['Count'], bottom=bottom, color=row['Color'], edgecolor='black')
    bottom += row['Count']


# Create legend with species names and corresponding colors
legend_patches = []
for species, color in zip(df['Species'], df['Color']):
    legend_patches.append(plt.Rectangle((0, 0), 1, 1, color=color, label=species))

plt.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5))

# Create Chart
plt.ylabel('Read Count per Species in Feces_Control', fontsize = 18)
plt.tight_layout()
plt.show()
