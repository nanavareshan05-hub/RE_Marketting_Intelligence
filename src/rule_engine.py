import pandas as pd

df = pd.read_csv("data/posts_sentiment.csv")

total = len(df)
negative_rate = len(df[df['sentiment'] == 'negative']) / total
avg_compound = df['compound'].mean()
severe_negative = df[df['compound'] <= -0.70]

print(f"Total posts: {total}")
print(f"Negative rate: {negative_rate:.2f}")
print(f"Avg compound: {avg_compound:.2f}")
print(f"Severe negative posts: {len(severe_negative)}")

rules = {}

if negative_rate > 0.25:
    rules['high_negative_rate'] = f"Negative posts at {negative_rate:.0%}, above 25% threshold"

if avg_compound < 0.15:
    rules['low_avg_sentiment'] = f"Average sentiment dropped to {avg_compound:.2f}, below 0.15 threshold"

if len(severe_negative) > 5:
    rules['severe_complaints'] = f"{len(severe_negative)} posts with compound below -0.70 detected"
    rules['top_complaints'] = severe_negative[['title', 'compound']].head(5).to_dict('records')

if rules:
    print("\nTriggered rules:")
    for rule, value in rules.items():
        print(f"  {rule}: {value}")
else:
    print("\nNo rules triggered — sentiment looks healthy")