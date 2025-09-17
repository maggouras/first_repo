import pandas as pd

# Load the Excel dataset
df = pd.read_excel('/Users/madelynaggouras/Downloads/Mantamonis_bacterial_contamination_analysis.xlsx')  # adjust the path

# Select only the desired columns
filtered = df[['contig ID', 'Seq Coverage']]

# Sort by Seq Coverage descending
filtered = filtered.sort_values(by='Seq Coverage', ascending=False)

# Keep only the first 5 rows
filtered = filtered.head(5)

# Save the filtered dataset as Excel in your repo
filtered.to_excel('filtered_mantamonis.xlsx', index=False)
