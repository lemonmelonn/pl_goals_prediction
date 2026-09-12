# Use for project after finish exam

from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

# # List of all seasons in the 21st century
# seasons = ["2000-01", "2001-02", "2002-03", "2003-04", "2004-05", "2005-06", "2006-07", "2007-08", "2008-09", "2009-10",
#            "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19",
#            "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25",]

# seasons = ["2000-01", "2001-02", "2002-03", "2003-04", "2004-05", "2005-06", "2006-07", "2007-08", "2008-09", "2009-10",
#            "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19"]

seasons = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]

for season in seasons:
    log = leaguegamelog.LeagueGameLog(
        season=season,
        season_type_all_star="Regular Season",
        player_or_team_abbreviation="T"
    )

    df = log.get_data_frames()[0]

    print(df.columns)

    # Print the first row (index 0) as a list
    print(df.iloc[0].tolist())

    df.to_csv(f"./data/{season}.csv")