import pandas as pd
import numpy as np

# Step 1: Read the dataset
csv_file_path = './student_activity_dataset.csv'  # Update the path
data = pd.read_csv(csv_file_path)

# Display the DataFrame
print("Student Activity Dataset:")
print(data)
