import os
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

df = pd.read_csv("data/posts_sentiment.csv")

total = len(df)
negative_rate = len(df[df['sentiment'] == 'negative']) / total
avg_compound = df['compound'].mean()
severe_negative = df[df['compound'] <= -0.70]

top_complaints = severe_negative[['title', 'compound']].head(5).to_dict('records')

prompt = f"""
You are a senior marketing strategist for Royal Enfield.

Here is the current sentiment data from r/royalenfield on Reddit:
- Total posts analyzed: {total}
- Negative post rate: {negative_rate:.0%}
- Average sentiment score: {avg_compound:.2f} (scale -1 to +1)
- Severely negative posts detected: {len(severe_negative)}

Top complaints:
{top_complaints}

Write a 3-part strategic recommendation:
1. What is happening (2 sentences, plain language)
2. Why it is happening (2-3 sentences based on the complaints)
3. What the marketing team should do this week (3 concrete actions, one sentence each)

Tone: direct, non-technical, actionable. No jargon.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

recommendation = response.choices[0].message.content
print(recommendation)

with open("output/recommendation.txt", "w") as f:
    f.write(recommendation)

print("\nSaved to output/recommendation.txt")