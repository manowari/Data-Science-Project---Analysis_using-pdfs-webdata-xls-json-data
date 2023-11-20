# unstructured_analysis.py
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy

nltk.download('vader_lexicon')  # Download the VADER sentiment lexicon for NLTK

def analyze_unstructured_data(text_data):
    # Tokenization
    tokens = tokenize_text(text_data)

    # Part-of-speech tagging
    pos_tags = pos_tagging(tokens)

    # Named Entity Recognition (NER)
    named_entities = named_entity_recognition(text_data)

    # Sentiment Analysis
    sentiment_result = perform_sentiment_analysis(text_data)

    result = {
        'tokens': tokens,
        'pos_tags': pos_tags,
        'named_entities': named_entities,
        'sentiment_analysis': sentiment_result
    }

    return result

def tokenize_text(text_data):
    # Tokenization using spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text_data)
    tokens = [token.text for token in doc]
    return tokens

def pos_tagging(tokens):
    # Part-of-speech tagging using spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(" ".join(tokens))
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

def named_entity_recognition(text_data):
    # Named Entity Recognition (NER) using spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text_data)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    return named_entities

def perform_sentiment_analysis(text_data):
    # Sentiment Analysis using NLTK's VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text_data)

    sentiment_result = {
        'compound_score': sentiment_scores['compound'],
        'positive_score': sentiment_scores['pos'],
        'negative_score': sentiment_scores['neg'],
        'neutral_score': sentiment_scores['neu']
    }

    return sentiment_result
