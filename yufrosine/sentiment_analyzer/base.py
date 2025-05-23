from abc import ABC, abstractmethod

class SentimentAnalyzer(ABC):
    @abstractmethod
    def get_score(self, text: str) -> float:
        """Return sentiment score from -1 to 1."""
        pass

    @abstractmethod
    def get_lable(self, text: str) -> str:
        """Return sentiment label: 'positive', 'neutral', or 'negative'."""
        pass
