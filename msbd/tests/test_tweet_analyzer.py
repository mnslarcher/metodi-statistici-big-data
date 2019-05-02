from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem.snowball import SnowballStemmer
from string import punctuation
from ..preprocessamento import tweet_analyzer
import pytest

tokenizer = TweetTokenizer(
    preserve_case=False,
    reduce_len=True,
    strip_handles=True
)
stemmer = SnowballStemmer("english")
stop_words = stopwords.words("english") + list(punctuation)


def test_ridurre_in_token():
    tweet = "test test"
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert isinstance(tweet, list)


def test_sostituire_tag_html():
    tweet = "&lt;3"
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert tweet == ["<3"]


def test_sostituire_collegamenti_ipertestuali():
    tweet = "fake http://www.fakelink.com"
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert tweet == ["fake", "link"]


def test_rimuovere_stop_words():
    tweet = "i am mario."
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert tweet == ["mario"]


def test_rimuovere_numeri():
    tweet = "dougla adam 42"
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert tweet == ["dougla", "adam"]


def test_ridurre_alla_radice():
    tweet = "completely successful"
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert tweet == ["complet", "success"]


def test_tweet_complicato():
    tweet = ("@student! analyze this &lt;3 tweeeet;, solution at "
        "http://www.fakelink.com :D 42 #42")
    tweet = tweet_analyzer(tweet, tokenizer, stemmer, stop_words)
    assert tweet == ["analyz", "<3", "tweeet", "solut", "link", ":d", "#42"]
