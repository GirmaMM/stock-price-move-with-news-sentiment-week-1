import pandas as pd
import re

def analyze_headline_length(data: pd.DataFrame) -> pd.Series:
    """Calculate descriptive statistics for headline lengths."""
    data['headline_length'] = data['headline'].apply(len)
    return data['headline_length'].describe()

def count_publisher_articles(data: pd.DataFrame) -> pd.Series:
    """Count articles by publisher."""
    return data['publisher'].value_counts()

def analyze_weekday_distribution(data: pd.DataFrame) -> pd.Series:
    """Count articles by day of week."""
    if not pd.api.types.is_datetime64_any_dtype(data['date']):
        raise ValueError("Date column must be datetime format")
    return data['date'].dt.day_name().value_counts()

def analyze_hourly_distribution(data: pd.DataFrame) -> pd.Series:
    """Count articles by hour of day."""
    if not pd.api.types.is_datetime64_any_dtype(data['date']):
        raise ValueError("Date column must be datetime format")
    return data['date'].dt.hour.value_counts().sort_index()

def extract_email_domain(email: str) -> str:
    """Extract domain from email address."""
    match = re.search(r"@([\w\.-]+)", email)
    return match.group(1) if match else None

def analyze_domain_distribution(data: pd.DataFrame) -> pd.DataFrame:
    """Count articles by publisher domain."""
    domains = data['publisher'].apply(extract_email_domain)
    return domains.value_counts().rename_axis('domain').reset_index(name='count')