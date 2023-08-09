#!/usr/bin/python3
"""
Recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces).
"""

import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API and counts keyword occurrences.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): List of keywords to count.
        after (str): The 'after' parameter for pagination.
        word_counts (dict): Dictionary to store word counts.

    Returns:
        None
    """
    if word_counts is None:
        word_counts = {}

    if after is None:
        sorted_counts = sorted(word_counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            count_words(subreddit, word_list, word_counts=word_counts)
            return

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    word_counts[word.lower()] = word_counts.get(word.lower(),
                                                                0) + 1

        after = data['data']['after']
        count_words(subreddit, word_list, after, word_counts)


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
