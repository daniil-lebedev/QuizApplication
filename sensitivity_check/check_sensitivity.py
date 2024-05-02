import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')
# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()


def analyze_text(text: str) -> dict:
    """
    Analyze the sentiment of a text using the VADER sentiment analyzer.
    :param text: The text to analyze.
    :return: A dictionary containing the sentiment scores.
    """
    scores = sia.polarity_scores(text)
    return scores


def is_offensive(text: str, threshold=-0.5) -> tuple:
    """
    Check if a text is offensive based on the compound sentiment score.
    :param text: the text to analyze
    :param threshold: the threshold for the compound score
    :return: a tuple containing a boolean indicating if the text is offensive and the sentiment scores
    """
    scores = analyze_text(text)
    if scores['compound'] <= threshold:
        return True, scores
    return False, scores
