#!/usr/bin/python3
"""
100-count.py
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    # Set a custom User-Agent header
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return count_occurrences(hot_list, word_list)
        else:
            after = data['data']['after']
            for post in posts:
                hot_list.append(post['data']['title'].lower())
            return count_words(subreddit, word_list, hot_list, after)
    else:
        return None


def count_occurrences(hot_list, word_list, counts={}):
    if not hot_list:
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1],
                                                                 item[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
    else:
        title = hot_list.pop()
        for word in word_list:
            if f" {word.lower()} " in f" {title} ":
                counts[word.lower()] = counts.get(word.lower(), 0) + 1
        return count_occurrences(hot_list, word_list, counts)


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
