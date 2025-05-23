from yufrosine import VaderAnalyzer, NewsApiSpaCyFetcher
from collections import defaultdict
import statistics


def calc_company_scores(cleaned_articles, analyzer):
    return analyzer.get_score_list_dict(cleaned_articles)


def calc_company_labels(cleaned_articles, analyzer):
    return analyzer.get_label_list_dict(cleaned_articles)


def calc_company_frequency(cleaned_articles):
    counts = defaultdict(int)
    for article in cleaned_articles:
        for company in article["companies"]:
            counts[company] += 1
    return dict(counts)


def run_demo():
    print("Fetching and analyzing articles...\n")
    
    fetcher = NewsApiSpaCyFetcher()
    analyzer = VaderAnalyzer()

    cleaned_articles = fetcher.company_and_article_list(100)

    print(f"Sample extracted articles (5 from {len(cleaned_articles)} total):")
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
    #print("Work in progress")


if __name__ == "__main__":
    run_demo()