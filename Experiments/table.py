import pandas as pd

# Define the data, applying realistic popularity scores for each category
data_full = {
    'Platform': [
                    'Instagram', 'Facebook', 'TikTok', 'YouTube',
                    'Instagram', 'Facebook', 'TikTok', 'YouTube',
                    'Instagram', 'Facebook', 'TikTok', 'YouTube',
                    'Instagram', 'Facebook', 'TikTok', 'YouTube',
                    'Instagram', 'Facebook', 'TikTok', 'YouTube',
                    'Instagram', 'Facebook', 'TikTok', 'YouTube',
                ] * 6,
    'Age Group': ['18-24', '18-24', '18-24', '18-24',
                  '25-34', '25-34', '25-34', '25-34',
                  '35-44', '35-44', '35-44', '35-44',
                  '45-54', '45-54', '45-54', '45-54',
                  '55-64', '55-64', '55-64', '55-64',
                  '65+', '65+', '65+', '65+'] * 6,
    'Continent': ['North America'] * 24 + ['Europe'] * 24 + ['Asia'] * 24 + ['Africa'] * 24 + ['South America'] * 24 + [
        'Oceania'] * 24,
    'Frequency': ['Daily', 'Weekly', 'Daily', 'Daily',
                  'Daily', 'Daily', 'Daily', 'Daily',
                  'Weekly', 'Daily', 'Weekly', 'Daily',
                  'Weekly', 'Daily', 'Weekly', 'Daily',
                  'Weekly', 'Weekly', 'Weekly', 'Daily',
                  'Weekly', 'Weekly', 'Weekly', 'Weekly'] * 6,
    'Preferences': ['Images, Reels', 'Images, Text', 'Short Videos', 'Long Videos',
                    'Reels, Ads', 'Groups, Marketplace', 'Short Videos', 'Videos',
                    'Business Tools', 'Family Connections', 'Trending Content', 'Videos',
                    'News, Family', 'Family, News', 'Trending', 'News, Videos',
                    'Family, News', 'Family', 'News, Entertainment', 'Entertainment, News',
                    'Family, Connections', 'News', 'News', 'Videos'] * 6,
    'Popularity Score': [
        # North America (sample scores)
        9, 6, 10, 8,  # 18-24
        8, 7, 9, 9,  # 25-34
        6, 8, 7, 8,  # 35-44
        5, 8, 6, 7,  # 45-54
        4, 6, 4, 6,  # 55-64
        3, 5, 2, 5,  # 65+

        # Europe
        8, 5, 9, 7,
        7, 6, 8, 8,
        6, 7, 6, 7,
        5, 6, 5, 6,
        4, 5, 3, 5,
        3, 4, 2, 4,

        # Asia
        8, 6, 8, 9,
        7, 6, 7, 8,
        6, 6, 6, 7,
        5, 5, 4, 6,
        4, 5, 3, 5,
        3, 4, 2, 4,

        # Africa
        7, 8, 7, 6,
        6, 8, 6, 7,
        5, 7, 5, 6,
        4, 6, 4, 5,
        4, 5, 3, 4,
        3, 4, 2, 3,

        # South America
        8, 7, 9, 8,
        7, 7, 8, 8,
        6, 7, 6, 7,
        5, 6, 5, 6,
        4, 5, 3, 5,
        3, 4, 2, 4,

        # Oceania
        9, 6, 10, 8,
        8, 7, 9, 9,
        7, 8, 7, 8,
        6, 7, 5, 7,
        5, 6, 4, 6,
        4, 5, 3, 5
    ]
}

# Creating the DataFrame
df_full = pd.DataFrame(data_full)

# Creating the pivot table with popularity scores by Platform, Age Group, and Continent
pivot_table_full = pd.pivot_table(df_full, values='Popularity Score', index=['Platform', 'Age Group'],
                                  columns=['Continent'], aggfunc='mean')

# Save to an Excel file
file_path_full = 'Social_Media_Usage_Full_R_with_Pivot.xlsx'

with pd.ExcelWriter(file_path_full, engine='xlsxwriter') as writer:
    df_full.to_excel(writer, sheet_name='Detailed Data', index=False)
    pivot_table_full.to_excel(writer, sheet_name='Pivot Table')

print(f"File saved successfully as {file_path_full}")
