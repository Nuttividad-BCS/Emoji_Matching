import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import emoji

sia = SentimentIntensityAnalyzer()

def get_emoji(sentiment_score):
    if sentiment_score >= 0.7:
        return emoji.emojize(":smiley:")
    elif sentiment_score > 0.5:
        return emoji.emojize(":slightly_smiling_face:")
    elif sentiment_score >= -0.2 and sentiment_score <= 0:
        return emoji.emojize(":neutral_face:")
    elif sentiment_score >= -0.75 and sentiment_score < -0.2:
        return emoji.emojize(":angry_face:")
    elif sentiment_score < -0.8:
        return emoji.emojize(":slightly_frowning_face:")

def analyze_text_with_emoji(text):
    sentiment = sia.polarity_scores(text)
    sentiment_score = sentiment['compound']
    matched_emoji = get_emoji(sentiment_score)
    return f"{text} {matched_emoji}"

test_sentences = [
    "I just won a prize, and I’m so excited!",
    "I love spending time with my family.",
    "I failed my test, and I feel so disappointed.",
    "Someone just cut me off in traffic, and I’m furious!",
    "I had an okay day, nothing too exciting."
]

for sentence in test_sentences:
    print(analyze_text_with_emoji(sentence))