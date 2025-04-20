import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file
data = pd.read_csv("D:/classwork/AI/Comp560FinalProject/WELFake_Dataset.csv") 

# Split into train/test (80/20)
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Shuffle both splits
train = train.sample(frac=1, random_state=42).reset_index(drop=True)
test = test.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSVs
train.to_csv("D:/classwork/AI/Comp560FinalProject/dataFixed/train.csv", index=False)
test.to_csv("D:/classwork/AI/Comp560FinalProject/dataFixed/test.csv", index=False)

# Confirm shapes
print("Train shape:", train.shape)
print("Test shape:", test.shape)
