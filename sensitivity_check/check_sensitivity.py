import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from better_profanity import profanity as bp

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


def contains_offensive_keywords(text: str) -> bool:
    """
    Check if text contains offensive keywords.
    """
    return bp.contains_profanity(text)


def is_offensive(text: str) -> dict:
    """
    Determine if text is offensive by combining keyword analysis and sentiment analysis.
    :param text: the text to analyze
    :return: a dictionary containing the result of the analysis
    """
    scores = analyze_text(text)
    print(scores)
    # Check for offensive keywords first
    if contains_offensive_keywords(text):
        return {'is_offensive': True, 'scores': scores, 'reason': bp.censor(text)}

    # using compound score to determine if the text is offensive
    elif scores['compound'] < -0.5:
        print(-0.5 > scores['compound'])
        return {'is_offensive': True, 'scores': scores,
                'reason': 'Negative sentiment, please write constructive feedback'}
    else:
        return {'is_offensive': False, 'scores': scores, 'reason': 'No offensive content detected'}
