# stat_analysis.py
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.pos_tag import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary libraries (nltk, wordnet, and Vader's Sentiment Lexicon)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('vader_lexicon')


def analyze_comments(comments):
  """
  Analyzes a list of student comments and identifies adjectives, adverbs, nouns, and sentiment.

  Args:
      comments (list): A list of strings representing comments.

  Returns:
      dict: A dictionary containing adjectives, adverbs, nouns, sentiment labels, and sentiment scores.
  """
  adjectives = []
  adverbs = []
  nouns = []
  sentiment_labels = []
  sentiment_analyzer = SentimentIntensityAnalyzer()

  for comment in comments:
    words = word_tokenize(comment)
    pos_tags = pos_tag(words)

    for word, tag in pos_tags:
      if tag.startswith('J'):
        adjectives.append(word.lower())
      elif tag.startswith('R'):
        adverbs.append(word.lower())
      elif tag.startswith('N'):
        nouns.append(word.lower())

    sentiment_scores = sentiment_analyzer.polarity_scores(comment)
    if sentiment_scores['compound'] >= 0.05:
      sentiment_labels.append('positive')
    elif sentiment_scores['compound'] <= -0.05:
      sentiment_labels.append('negative')
    else:
      sentiment_labels.append('neutral')

  results = {
      'adjectives': list(set(adjectives)),
      'adverbs': list(set(adverbs)),
      'nouns': list(set(nouns)),
      'sentiment': sentiment_labels,
      'sentiment_scores': sentiment_scores
  }
  return results

def compare_projects(first_project_comments, final_project_comments):
  """
  Compares the use of adjectives, adverbs, nouns, and sentiment between first and final project comments.

  Args:
      first_project_comments (list): List of comments from the first project.
      final_project_comments (list): List of comments from the final project.

  Returns:
      dict: A dictionary containing the comparison results for adjectives, adverbs, nouns, and sentiment.
  """
  first_project_analysis = analyze_comments(first_project_comments)
  final_project_analysis = analyze_comments(final_project_comments)

  comparison_results = {
      'adjectives': {
          'first_project': first_project_analysis['adjectives'],
          'final_project': final_project_analysis['adjectives']
      },
      'adverbs': {
          'first_project': first_project_analysis['adverbs'],
          'final_project': final_project_analysis['adverbs']
      },
      'nouns': {
          'first_project': first_project_analysis['nouns'],
          'final_project': final_project_analysis['nouns']
      },
      'sentiment': {
          'first_project': first_project_analysis['sentiment'],
          'final_project': final_project_analysis['sentiment']
      },
      'sentiment_scores': {
          'first_project': first_project_analysis['sentiment_scores'],
          'final_project': final_project_analysis['sentiment_scores']
      }
  }
  return comparison_results

# Example usage
if __name__ == "__main__":
  first_project_comments = [
      "This assignment was confusing.",
      "I need help with the code."
  ]
  final_project_comments = [
      "This project was challenging, but I learned a lot.",
      "The final code works well!"
  ]
  comparison_result = compare_projects(first_project_comments, final_project_comments)

  print("Adjectives Comparison:")
  print("  First Project:", comparison_result['adjectives']['first_project'])
  print("  Final Project:", comparison_result['adjectives']['final_project
