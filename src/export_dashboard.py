import pandas as pd

df = pd.read_csv("data/posts_sentiment.csv")

df['date'] = pd.to_datetime(df['created_utc'], unit='s')
df['date_only'] = df['date'].dt.date

dashboard_df = df[['title', 'text', 'sentiment', 'compound', 'pos', 'neu', 'neg', 'date_only', 'score', 'num_comments']]

dashboard_df.to_csv("output/dashboard_data.csv", index=False)
print(f"Exported {len(dashboard_df)} rows to output/dashboard_data.csv")