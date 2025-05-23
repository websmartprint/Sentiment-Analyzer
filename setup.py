from setuptools import setup, find_packages

setup(
    name="yufrosine",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "spacy",
        "pandas",
        #"textblob",
        "vaderSentiment",
        "newsapi-python"
    ],
    python_requires=">=3.8"
)
