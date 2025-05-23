from .base import SentimentAnalyzer
from .util import score_to_good_bad_rating
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class VaderAnalyzer(SentimentAnalyzer):
    def get_score(self, text: str) -> float:
        analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(text)['compound']

    def get_lable(self, text: str) -> str:
        return score_to_good_bad_rating(self.get_score(text))

