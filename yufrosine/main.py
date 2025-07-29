from yufrosine import VaderAnalyzer, NewsApiSpaCyFetcher
from collections import defaultdict
import statistics
import os

# Prints yusofren in ascci, only for aestheics in the command line when testing
#Takes ascci title from a txt doc
def print_title():
    print("Current working directory:", os.getcwd())
    filepath = "yufrosine/header.txt"

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#calculates the company scores from -1 to 1
# takes the cleaned articles list of dictionaries from the fetcher, as well as the analysis model to be used
def calc_company_scores(cleaned_articles, analyzer):
    return analyzer.get_score_list_dict(cleaned_articles)

#calculates the company scores from very bad, bad, neutral, good, very good
# takes the cleaned articles list of dictionaries from the fetcher, as well as the analysis model to be used
def calc_company_labels(cleaned_articles, analyzer):
    return analyzer.get_label_list_dict(cleaned_articles)

# Mainly fo resting, gives the freqency of companies found, takes the cleaned artile lst of dictionaries from fetcher
def calc_company_frequency(cleaned_articles):
    counts = defaultdict(int)
    for article in cleaned_articles:
        for company in article["companies"]:
            counts[company] += 1
    return dict(counts)

# runs the full analysis on the articles and gives a list of dictionaries with reults
# article pool - Initial number of articles analized, only a small percent of these are actually in the final analysis as not all articles containmentions of important companies
# analyer - choose analysis model, vader is only current, fibert will be added
# fetcher - choose article filter model and article fetcher, spacy is only current
# mode - numeric gives scores from -1 to 1, written gives a written score from very bad, bad, neutral, ood, very good
def run_analysis(article_pool = 100, analyzer = "vader", fetcher = "spacy", mode = "numeric"):

    # will add if staments later when more fetchers are available
    fetcher = NewsApiSpaCyFetcher()

    #will add if stsmanets when more fetchers are available
    analyzer = VaderAnalyzer()

    #fetch and filter articles from pool
    cleaned_articles = fetcher.company_and_article_list(article_pool)

    #return sentiments with scores
    if mode == "numeric":
        return calc_company_scores(cleaned_articles, analyzer)

    #returns sentiments with written rating
    return calc_company_labels(cleaned_articles, analyzer)



# Used for testing and demo purposes
#Runs and prints each step of the analysis
def run_demo():
    print_title()

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