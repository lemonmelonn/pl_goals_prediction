import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./preparation/finalclean.csv")
df = pd.read_csv("./preparation/opponentvalues.csv")

df = df[['TEAM_ABBREVIATION', 'HOME', 'PREV_WIN', 'PREV_PTS', 'PREV_PLUSMINUS', 'ROLL3_PTS', 'ROLL3_PLUS_MINUS', 
        'ROLL3_FG_PCT', 'ROLL3_REB', 'ROLL3_AST', 'ROLL3_TOV', 'WIN_STREAK', 'LOSE_STREAK', 'DAYS_REST', 
        'IS_BACK_TO_BACK', 'SEASON_WIN_PCT', 'ELO', 'OPP', 'OPP_PREV_WIN', 'OPP_PREV_PTS', 'OPP_PREV_PLUSMINUS', 'OPP_WIN_STREAK', 
        'OPP_LOSE_STREAK', 'OPP_DAYS_REST', 'OPP_IS_BACK_TO_BACK', 'OPP_SEASON_WIN_PCT', 'OPP_ELO',
        'OPP_ROLL3_PTS', 'OPP_ROLL3_PLUS_MINUS', 'OPP_ROLL3_FG_PCT', 'OPP_ROLL3_REB', 'OPP_ROLL3_AST', 
        'OPP_ROLL3_TOV', 'ELO_DIFF', 'SEASON_WIN_PCT_DIFF', 'ROLL3_PLUS_MINUS_DIFF', 'ROLL3_FG_PCT_DIFF',
        'ROLL3_PTS_DIFF', 'ROLL3_REB_DIFF', 'PREV_PLUSMINUS_DIFF',
        'PREV_PTS_DIFF', 'WIN_STREAK_DIFF', 'WIN']]

df = df[['TEAM_ABBREVIATION', 'HOME', 'PREV_WIN', 'PREV_PTS', 'ROLL3_PTS',
        'ROLL3_FG_PCT', 'ROLL3_REB', 'ROLL3_AST', 'ROLL3_TOV', 'WIN_STREAK', 'LOSE_STREAK', 'DAYS_REST', 
        'IS_BACK_TO_BACK', 'OPP', 'OPP_PREV_WIN', 'OPP_PREV_PTS', 'OPP_WIN_STREAK', 
        'OPP_LOSE_STREAK', 'OPP_DAYS_REST', 'OPP_IS_BACK_TO_BACK',
        'OPP_ROLL3_FG_PCT', 'OPP_ROLL3_REB', 'OPP_ROLL3_AST', 
        'OPP_ROLL3_TOV', 'ELO_DIFF', 'SEASON_WIN_PCT_DIFF', 'ROLL3_PLUS_MINUS_DIFF', 'ROLL3_FG_PCT_DIFF',
        'ROLL3_PTS_DIFF', 'ROLL3_REB_DIFF', 'PREV_PLUSMINUS_DIFF',
        'PREV_PTS_DIFF', 'WIN_STREAK_DIFF', 'WIN']]

# df = df[['ELO_DIFF', "SEASON_WIN_PCT_DIFF", "WIN"]]

# Split the data into features and target variable
X = df.drop(columns=["WIN"])
y = df['WIN']

df.to_csv("./modeldata/modeldata.csv")

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Save the training, validation, and test sets to CSV files
train_df = X_train.copy()
train_df['WIN'] = y_train
train_df.to_csv("./modeldata/train.csv", index=False)

test_df = X_test.copy()
test_df['WIN'] = y_test
test_df.to_csv("./modeldata/test.csv", index=False)