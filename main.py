import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("C:/Users/Dell/Desktop/Air_Quality.csv")

# Remove duplicates
data = data.drop_duplicates()

# Drop unnecessary columns
data = data.drop(columns=["Unique ID", "Indicator ID", "Measure", "Measure Info", "Message"])

data["Start_Date"] = pd.to_datetime(data["Start_Date"], format="%m/%d/%Y")

# Remove rows with missing values
data = data.dropna()

# Save the preprocessed dataset to a new CSV file
data.to_csv('preprocessed_air_quality.csv', index=False)

