import asyncio
from datetime import datetime, timedelta
import pandas as pd
from nbainjuries import injury_asy

async def fetch_injury_history(start_date, end_date, interval_days=1):
    """
    Asynchronously fetches NBA injury data reports between start_date and end_date.
    """
    all_reports = []
    current_date = start_date
    
    while current_date <= end_date:
        # Targeting standard pre-game report slots (e.g., 17:00 ET)
        report_time = current_date.replace(hour=17, minute=30, second=0)
        
        try:
            print(f"Fetching report for: {report_time.strftime('%Y-%m-%d %H:%M')}")
            # Fetch data as a Pandas DataFrame directly
            df = await injury_asy.get_reportdata_async(report_time, return_df=True)
            
            if df is not None and not df.empty:
                all_reports.append(df)
        except Exception as e:
            # Handles days without reports (e.g., off-season dates) gracefully
            print(f"No report or error for {report_time.strftime('%Y-%m-%d')}: {e}")
            
        current_date += timedelta(days=interval_days)
        
    if all_reports:
        return pd.concat(all_reports, ignore_index=True)
    return pd.DataFrame()

async def main():
    # Define your timeframe (adjust ranges or step size as necessary)
    start = datetime(2021, 10, 22) # Opening of 2019-20 season
    end = datetime(2026, 4, 15)   # End of regular season/play-in window
    
    master_df = await fetch_injury_history(start, end, interval_days=1)
    
    if not master_df.empty:
        # Save to CSV for your modeling or exploratory data analysis
        master_df.to_csv("nba_injuries_2019_2026.csv", index=False)
        print(f"Successfully saved {len(master_df)} total records to CSV.")
    else:
        print("No records retrieved.")

# Run the async loop
if __name__ == "__main__":
    asyncio.run(main())