import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("data/posts_cleaned.csv")

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    scores = analyzer.polarity_scores(str(text))
    compound = scores['compound']
    
    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"
    
    return pd.Series({
        'compound': compound,
        'pos': scores['pos'],
        'neu': scores['neu'],
        'neg': scores['neg'],
        'sentiment': label
    })

df[['compound', 'pos', 'neu', 'neg', 'sentiment']] = df['text'].apply(get_sentiment)

print(df['sentiment'].value_counts())
print("\nSample results:")
print(df[['title', 'sentiment', 'compound']].head(10))

df.to_csv("data/posts_sentiment.csv", index=False)
print("\nSaved sentiment data")