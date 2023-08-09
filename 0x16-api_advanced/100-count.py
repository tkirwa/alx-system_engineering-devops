#!/usr/bin/python3
"""
Module for a function that queries the Reddit API recursively.
"""

import requests


def count_words(subreddit, word_list, after=None, word_dict=None):
    """Recursively queries the Reddit API and counts keyword occurrences."""
    if word_dict is None:
        word_dict = {}

    if after is None:
        sorted_counts = sorted(word_dict.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
