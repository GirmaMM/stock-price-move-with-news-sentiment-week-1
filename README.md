# Stock Price Movement Prediction Using News Sentiment

**Week 1 Challenge – 10 Academy AI Mastery**

## Overview

This project analyzes **financial news sentiment** and its correlation with stock price movements. Using **NLP techniques** and **quantitative analysis**, we derive insights that aid in **predictive market forecasting**.

## Key Objectives

* **Sentiment Analysis:** Extract sentiment scores from headlines.
* **Technical Indicators:** Compute RSI, MACD, and Moving Averages using TA-Lib.
* **Stock Price Correlation:** Analyze sentiment-driven market movements.

## Dataset

* **Stock dataset from yfinance:** [https://drive.google.com/file/d/1j2c7mAgaPFSJ6HedekjqVugbDRCs29wd/view?usp=drive_link](https://drive.google.com/file/d/1j2c7mAgaPFSJ6HedekjqVugbDRCs29wd/view?usp=drive_link)
* **Raw data for sentiment analysis:** [https://drive.google.com/file/d/1x1BKCV5F6HpDQwnYfNM8kN517j6sHDSt/view?usp=drive_link](https://drive.google.com/file/d/1x1BKCV5F6HpDQwnYfNM8kN517j6sHDSt/view?usp=drive_link)

## Project Structure
📂 stock-price-move-with-news-sentiment-week-1 ├── .vscode/ ├── .github/ │   └── workflows/ │       └── unittests.yml      # GitHub Actions workflow for unit tests ├── .gitignore                 # Files and directories to ignore in Git ├── requirements.txt           # Dependencies for Python environment ├── README.md                  # Project documentation ├── notebooks/ │   ├── correlation_analysis.py │   ├── eda_stock_news.ipynb  # Jupyter notebook for stock news analysis │   ├── quantitative_analysis.ipynb # Financial insights notebook ├── scripts/ │   ├── descriptive_analysis.py  # Analyzes news publications │   ├── sentiment_analysis.py  # Extracts sentiment scores │   ├── stock_indicator.py  # computte stock indicator metrics │   ├── ts_analysis.py  # Provides statistical time series insights │   ├── init.py │   ├── README.md  # Documentation for scripts directory


## Installation & Setup

To set up the environment, run the following commands:

```bash
git clone [https://github.com/GirmaMM/stock-price-move-with-news-sentiment-week-1.git](https://github.com/GirmaMM/stock-price-move-with-news-sentiment-week-1.git)
cd stock-price-move-with-news-sentiment-week-1
pip install -r requirements.txt


## **How to Run**
```python 
python scritps/sentiment_analysis.py


### To perform sentiment analysis:
```python 
    python scripts/sentiment_analysis.py
    
### To compute stock indicators:
```python 
python src/stock_indicators.py



**Improve Results & Insights Section**  
```markdown
## Results & Insights
✔ Sentiment analysis reveals strong correlation between financial news and stock trends.
✔ Positive headlines often align with stock price increases, while negative headlines signal potential declines.
✔ Technical indicators, such as RSI and MACD, confirm market reactions to news sentiment.