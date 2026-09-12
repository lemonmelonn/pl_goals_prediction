import pandas as pd

# Load dataset
df = pd.read_csv("./preparation/allseasons.csv")
# df = pd.read_csv("./data/2025-26.csv")
print(df.shape)

# Format date
df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])

# Sort date
df = df.sort_values(by='GAME_DATE', ascending=True)

# Move column to first index
df.insert(0, 'GAME_DATE', df.pop('GAME_DATE'))

# Move column to first index
df.insert(1, 'GAME_ID', df.pop('GAME_ID'))

# Save to csv
df.to_csv("./preparation/firstclean.csv", index=False)
print(df.shape)