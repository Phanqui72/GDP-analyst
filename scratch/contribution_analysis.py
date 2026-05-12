import pandas as pd
import numpy as np

# Load data
sectors_df = pd.read_csv(r'd:\Data Analyst\GDP-Analyst\data\processed\gdp_sectors_processed.csv')
sectors_df.columns = ['Year', 'Total', 'Sector_I', 'Sector_II', 'Sector_III', 'Tax']

# Calculate Yearly Increase (Absolute)
for col in ['Sector_I', 'Sector_II', 'Sector_III']:
    sectors_df[f'{col}_Diff'] = sectors_df[col].diff()

# Calculate Contribution to Growth (Percentage Points - p.p)
# Contribution_i = (V_i(t) - V_i(t-1)) / Total(t-1) * 100
sectors_df['GDP_Prev'] = sectors_df['Total'].shift(1)
sectors_df['Cont_I'] = (sectors_df['Sector_I_Diff'] / sectors_df['GDP_Prev']) * 100
sectors_df['Cont_II'] = (sectors_df['Sector_II_Diff'] / sectors_df['GDP_Prev']) * 100
sectors_df['Cont_III'] = (sectors_df['Sector_III_Diff'] / sectors_df['GDP_Prev']) * 100

# Total Growth check
sectors_df['Total_Growth'] = sectors_df['Total'].pct_change() * 100

# Focus on Crisis Years
crisis_years = [1997, 1998, 1999, 2007, 2008, 2009, 2019, 2020, 2021]
analysis = sectors_df[sectors_df['Year'].isin(crisis_years)].copy()

print("Quantitative Contribution Analysis (Percentage Points):")
cols = ['Year', 'Total_Growth', 'Cont_I', 'Cont_II', 'Cont_III']
print(analysis[cols].to_string(index=False))

# Identify which sector's contribution dropped the most compared to previous year
analysis['Cont_II_Change'] = analysis['Cont_II'].diff()
analysis['Cont_III_Change'] = analysis['Cont_III'].diff()

def find_driver(row):
    if row['Cont_II_Change'] < row['Cont_III_Change']:
        return "Sector II (Industry)"
    else:
        return "Sector III (Service)"

# Only for drop years
drops = [1998, 2008, 2009, 2020]
print("\nDriver of the Growth Slowdown (Based on Contribution Change):")
for y in drops:
    row = analysis[analysis['Year'] == y].iloc[0]
    print(f"Year {y}: {find_driver(row)} led the slowdown in contribution.")
