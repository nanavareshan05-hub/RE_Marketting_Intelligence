# Royal Enfield — Marketing Intelligence System

Automated pipeline that monitors brand sentiment on Reddit, flags complaint patterns, and generates weekly marketing recommendations using an LLM.

## Overview

Most sentiment tools tell you what happened. This one tells you what to do about it.

The pipeline collects posts from r/royalenfield every week, classifies sentiment, runs them through a rule engine to detect when something is off, and uses an LLM to write a plain-language brief for the marketing team — no data background required to read it.

## Pipeline

Reddit JSON → Sentiment Analysis (VADER) → Rule Engine → Groq LLM → Power BI Dashboard

**collect_data.py** — Fetches 500+ posts from r/royalenfield using Reddit's public JSON endpoint. Paginates through results and saves raw data as CSV.

**sentiment_analysis.py** — Runs each post through VADER to classify it as positive, negative, or neutral using the compound score.

**rule_engine.py** — Checks three thresholds: negative rate, average sentiment score, and count of severely negative posts. Only triggered rules get passed forward.

**recommend.py** — Sends triggered rules and top complaints to Groq LLM. Returns a 3-part recommendation: what's happening, why, and what the marketing team should do this week.

**export_dashboard.py** — Exports a clean CSV for Power BI and saves the recommendation as a text file.

**pipeline.py** — Runs all five scripts in sequence. Scheduled via cron job every Monday at 9am.



## Results (sample run — 500 posts)

| Metric | Value |
|--------|-------|
| Positive posts | 297 (59%) |
| Neutral posts | 116 (23%) |
| Negative posts | 87 (17%) |
| Severe complaints flagged | 18 |
| Avg. sentiment score | 0.31 / 1.0 |

Top complaints detected: service center issues, ECU failures, panel gaps on new bikes.


## Tech Stack

| Tool | Why |
|------|-----|
| Python | Core language |
| Reddit JSON | Free, no auth required |
| VADER | Built for social media text, no training needed |
| Rule Engine | Makes detection auditable and explainable |
| Groq LLM (LLaMA 3.3-70b) | Free API, fast, good enough for recommendation generation |
| Power BI | Standard BI tool, readable by non-technical stakeholders |
| Cron | Weekly automation |


## Limitations

- VADER misclassifies sarcasm and image posts with no body text
- Currently Reddit-only — no cross-platform signal
- Power BI refresh is manual on Windows after each pipeline run


## Setup

```bash
git clone https://github.com/nanavareshan05-hub/RE_Marketting_Intelligence.git
cd RE_Marketting_Intelligence
pip3 install requests pandas vaderSentiment groq python-dotenv
```

Add a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Run:
```bash
python3 src/pipeline.py
```

Free Groq API key at https://console.groq.com

---

Built by Eshaan Nanavare