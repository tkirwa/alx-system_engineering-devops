#!/usr/bin/python3
"""
This script retrieves hot articles from a specified subreddit
 using the Reddit API,
counts occurrences of keywords in their titles, and prints the results.
"""
from requests import request


def count_words(subreddit, word_list, after="", counter=None, ini=0):
    """A recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not)
    """
    if counter is None:
        counter = {}

    if ini == 0:
        for word in word_list:
            counter[word] = 0

    url = f"https://api.reddit.com/r/{subreddit}/hot?after={after}"
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()

    try:
        top = response['data']['children']
        _after = response['data']['after']
        for item in top:
            for word in counter:
                counter[word] += (
                    item['data']['title'].lower().split(' ').
                    count(word.lower())
                    )
        if _after is not None:
            count_words(subreddit, word_list, _after, counter, 1)
        else:
            sorted_counts = sorted(counter.items(), key=lambda kv: (-kv[1],
                                                                    kv[0]))
            for name, num in sorted_counts:
                if num != 0:
                    print('{}: {}'.format(name, num))
    except Exception:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
