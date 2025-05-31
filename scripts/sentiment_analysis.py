# src/sentiment_analysis.py
import pandas as pd
import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import string

# NLTK setup
nltk.download(['punkt', 'stopwords', 'vader_lexicon'])

class SentimentAnalyzer:
    
    @staticmethod
    def analyze_sentiment(headlines: pd.Series) -> pd.DataFrame:
        """Analyze headlines using VADER sentiment analysis."""
        sia = SentimentIntensityAnalyzer()
        sentiments = headlines.apply(sia.polarity_scores)
        return pd.concat([headlines, pd.DataFrame(sentiments.tolist())], axis=1)

    @staticmethod
    def categorize_sentiment(score: float) -> str:
        """Classify sentiment as Positive/Neutral/Negative for a single score."""
        if not isinstance(score, (int, float)):
            raise ValueError("Input must be a numeric score")
        return 'Positive' if score >= 0.05 else 'Negative' if score <= -0.05 else 'Neutral'
    
    @staticmethod
    def apply_sentiment_categories(df: pd.DataFrame) -> pd.DataFrame:
        """Apply sentiment categories to a DataFrame with compound scores."""
        if 'compound' not in df.columns:
            raise ValueError("DataFrame must contain 'compound' column")
        df['sentiment'] = df['compound'].apply(SentimentAnalyzer.categorize_sentiment)
        return df

    @staticmethod
    def preprocess_text(text: str) -> str:
        """Clean text by removing punctuation, stopwords, and non-alphabetic chars."""
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'[^a-z\s]', '', text)
        words = [w for w in nltk.word_tokenize(text) if w not in stopwords.words('english')]
        return ' '.join(words)

    @staticmethod
    def get_common_keywords(headlines: pd.Series, top_n: int = 20) -> list[tuple[str, int]]:
        """Extract top N keywords from headlines."""
        cleaned = headlines.apply(SentimentAnalyzer.preprocess_text)
        return Counter(' '.join(cleaned).split()).most_common(top_n)

    @staticmethod
    def plot_wordcloud(word_freq: Counter) -> None:
        """Generate word cloud visualization."""
        wc = WordCloud(width=800, height=400, background_color='white')
        wc.generate_from_frequencies(word_freq)
        plt.figure(figsize=(10, 8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    @staticmethod
    def calculate_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
        """Compute daily average sentiment scores by stock."""
        return df.groupby(['Date', 'stock'])[['neg', 'neu', 'pos']].mean().reset_index()

    @staticmethod
    def plot_sentiment_trend(data: pd.DataFrame, stock: str) -> plt.Figure:
        """Visualize sentiment trend for a specific stock."""
        stock_data = data[data['stock'] == stock]
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for col, color in [('neg', 'red'), ('neu', 'grey'), ('pos', 'green')]:
            ax.plot(stock_data['Date'], stock_data[col], label=f'{col.capitalize()} Sentiment', color=color)
        
        ax.set(title=f'Sentiment Trend: {stock}', xlabel='Date', ylabel='Score')
        ax.legend()
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return fig