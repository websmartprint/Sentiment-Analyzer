from yufrosine import VaderAnalyzer, NewsApiSpacyFetcher
from collections import defaultdict
import statistics


def calc_company_scores(cleaned_articles, analyzer):
    sentiment_scores = defaultdict(list)

    for article in cleaned_articles:
        title = article.get("title", "")
        description = article.get("description", "")
        combined_text = f"{title}. {description}"

        score = analyzer.get_score(combined_text)

        for company in article["companies"]:
            sentiment_scores[company].append(score)

    return {
        company: statistics.mean(scores)
        for company, scores in sentiment_scores.items()
    }


def calc_company_labels(cleaned_articles, analyzer):
    sentiment_scores = defaultdict(list)

    for article in cleaned_articles:
        title = article.get("title", "")
        description = article.get("description", "")
        combined_text = f"{title}. {description}"

        score = analyzer.get_score(combined_text)

        for company in article["companies"]:
            sentiment_scores[company].append(score)

    return {
        company: analyzer.get_lable(statistics.mean(scores))
        for company, scores in sentiment_scores.items()
    }


def calc_company_frequency(cleaned_articles):
    counts = defaultdict(int)
    for article in cleaned_articles:
        for company in article["companies"]:
            counts[company] += 1
    return dict(counts)


def run_demo():
    print("Fetching and analyzing articles...\n")
    
    fetcher = NewsApiSpacyFetcher()
    analyzer = VaderAnalyzer()

    cleaned_articles = fetcher.company_and_article_list(100)

    print("Sample extracted articles:")
    for article in cleaned_articles[:5]:
        print(f"Title: {article['title']}")
        print(f"Companies: {article['companies']}")
        print("---")

    print("\n--- Company Frequency ---")
    freq = calc_company_frequency(cleaned_articles)
    print(freq)

    print("\n--- Company Sentiment Scores ---")
    scores = calc_company_scores(cleaned_articles, analyzer)
    print(scores)

    print("\n--- Company Sentiment Ratings ---")
    ratings = calc_company_labels(cleaned_articles, analyzer)
    print(ratings)


if __name__ == "__main__":
    run_demo()