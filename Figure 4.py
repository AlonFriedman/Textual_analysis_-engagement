import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_comments(comments):
    """
    Analyzes comments to count adjectives, adverbs, and nouns.

    Args:
        comments (list of str): The comments to analyze.

    Returns:
        A dictionary with counts of adjectives, adverbs, and nouns.
    """
    counts = {'adjectives': 0, 'adverbs': 0, 'nouns': 0}
    for comment in comments:
        tokens = word_tokenize(comment)
        tagged = pos_tag(tokens)
        for word, tag in tagged:
            if tag.startswith('J'):
                counts['adjectives'] += 1
            elif tag.startswith('R'):
                counts['adverbs'] += 1
            elif tag.startswith('N'):
                counts['nouns'] += 1
    return counts

def process_data(df):
    """
    Processes the DataFrame to get counts per project type and year.

    Args:
        df (DataFrame): The DataFrame containing comments, project types, and years.

    Returns:
        A processed DataFrame with counts.
    """
    result = []

    for year in [2019, 2020, 2021]:
        for project_type in ['first', 'final']:
            comments = df[(df['Year'] == year) & (
