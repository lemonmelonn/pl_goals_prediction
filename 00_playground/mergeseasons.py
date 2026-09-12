from glob import glob
import os
import pandas as pd

# Define path to your folder containing the CSV files
folder_path = "./data"

# Find all CSV files in the directory
all_files = glob(os.path.join(folder_path, "*.csv"))

# Read each file into a list of DataFrames, optionally ignoring/dropping unnamed index columns
df_list = []
for filename in all_files:
  temp_df = pd.read_csv(filename)
  # Drop any accidental unnamed index columns if present
  temp_df = temp_df.loc[:, ~temp_df.columns.str.contains("^Unnamed")]
  df_list.append(temp_df)

# Concatenate all dataframes vertically into a single master dataframe
master_df = pd.concat(df_list, ignore_index=True)

print(f"Successfully merged {len(all_files)} files.")
print("Master dataframe shape:", master_df.shape)
master_df.to_csv("./preparation/allseasons.csv", index=False)