import pytest
import pandas as pd

def test_stock_data_loading():
    df = pd.read_csv("data/stock_prices.csv")
    assert "Close" in df.columns