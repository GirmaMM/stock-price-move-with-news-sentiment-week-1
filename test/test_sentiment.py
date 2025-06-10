import pytest
from scripts.sentiment_analysis import analyze_sentiment

def test_sentiment_analysis():
    assert analyze_sentiment("This is great!") > 0
    assert analyze_sentiment("Terrible experience.") < 0