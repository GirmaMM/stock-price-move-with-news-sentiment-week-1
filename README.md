
# Stock Price Movement Prediction Using News Sentiment  
**Week 1 Challenge – 10 Academy AI Mastery**  

## Overview  
This project analyzes **financial news sentiment** and its correlation with stock price movements. Using **NLP techniques** and **quantitative analysis**, we derive insights to aid in **predictive market forecasting**.  

---

## Key Objectives  
- **Sentiment Analysis:** Extract sentiment scores from headlines.  
- **Technical Indicators:** Compute RSI, MACD, and Moving Averages using TA-Lib.  
- **Stock Price Correlation:** Analyze sentiment-driven market movements.  

---

## Dataset  
- **Stock Data (YFinance):** [Download Link](https://drive.google.com/file/d/1j2c7mAgaPFSJ6HedekjqVugbDRCs29wd/view?usp=drive_link)  
- **Sentiment Analysis Raw Data:** [Download Link](https://drive.google.com/file/d/1x1BKCV5F6HpDQwnYfNM8kN517j6sHDSt/view?usp=drive_link)  

---

## Project Structure  
```plaintext
📂 stock-price-move-with-news-sentiment-week-1  
├── .vscode/  
├── .github/  
│   └── workflows/  
│       ├── unittests.yml          # GitHub Actions workflow for unit tests  
│       ├── ci.yml                 # CI workflow for automated testing  
├── .gitignore                     # Files/directories ignored by Git  
├── requirements.txt               # Python dependencies  
├── README.md                      # Project documentation  
├── notebooks/  
│   ├── correlation_analysis.py  
│   ├── eda_stock_news.ipynb       # Exploratory analysis of stock news  
│   ├── quantitative_analysis.ipynb # Financial metrics analysis  
├── scripts/  
│   ├── descriptive_analysis.py    # News publication trends  
│   ├── sentiment_analysis.py      # Sentiment scoring  
│   ├── stock_indicator.py         # Technical indicators (RSI, MACD, etc.)  
│   ├── ts_analysis.py             # Time-series statistical insights  
│   ├── __init__.py  
│   ├── README.md                  # Scripts documentation  
```

---

## Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/GirmaMM/stock-price-move-with-news-sentiment-week-1.git
   cd stock-price-move-with-news-sentiment-week-1
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run  
### Sentiment Analysis:  
```bash
python scripts/sentiment_analysis.py
```  
### Stock Indicators Calculation:  
```bash
python scripts/stock_indicator.py
```  

---

## Continuous Integration & Deployment (CI/CD)  
Automated testing via **GitHub Actions** ensures:  
✅ Dependency installation  
✅ Unit test execution on every push/PR  
✅ Pre-merge error detection  

### Workflow Files:  
- `.github/workflows/ci.yml`  
- `.github/workflows/unittests.yml`  

### Run Tests Locally:  
```bash
pytest tests/
```  

---

## Results & Insights  
✔ **Sentiment-driven trends:** Positive news correlates with price increases; negative news precedes declines.  
✔ **Technical confirmation:** RSI, MACD, and Moving Averages align with sentiment shifts.  
✔ **Future work:** Integrate ML models for enhanced prediction accuracy.  