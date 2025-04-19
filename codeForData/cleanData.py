import pandas as pd
from sklearn.model_selection import train_test_split

# Load your CSV files
fake = pd.read_csv("D:/classwork/AI/Comp560FinalProject/data/importedDatasets/Fake.csv") 
true = pd.read_csv("D:/classwork/AI/Comp560FinalProject/data/importedDatasets/True.csv")  

# Label the data
fake['label'] = 0
true['label'] = 1

# Split each into train/test (80/20)
fake_train, fake_test = train_test_split(fake, test_size=0.2, random_state=3)
true_train, true_test = train_test_split(true, test_size=0.2, random_state=3)

# Combine fake and true parts
train = pd.concat([fake_train, true_train]).sample(frac=1, random_state=3).reset_index(drop=True)
test = pd.concat([fake_test, true_test]).sample(frac=1, random_state=3).reset_index(drop=True)

# Save to CSVs
train.to_csv("D:/classwork/AI/Comp560FinalProject/data/cleanedData/train.csv", index=False)
test.to_csv("D:/classwork/AI/Comp560FinalProject/data/cleanedData/test.csv", index=False)

# Confirm shapes
print("Train shape:", train.shape)
print("Test shape:", test.shape)

