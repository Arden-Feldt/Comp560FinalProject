import pandas as pd

# Load the CSV files
fake = pd.read_csv("D:/classwork/AI/Comp560FinalProject/data/importedDatasets/Fake.csv") 
true = pd.read_csv("D:/classwork/AI/Comp560FinalProject/data/importedDatasets/True.csv")  

# Add labels
fake['label'] = 0
true['label'] = 1

# Combine and shuffle
combined = pd.concat([fake, true]).sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
combined.to_csv("D:/classwork/AI/Comp560FinalProject/data/combined.csv", index=False)

# Show first few rows
print(combined.head())


