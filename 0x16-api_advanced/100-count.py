#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of
 all hot articles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    if after is None:
        headers = {'User-Agent': 'MyBot/1.0'}
        params = {'limit': 100}
    else:
        headers = {'User-Agent': 'MyBot/1.0', 'after': after}
        params = {'limit': 100, 'after': after}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after', None)
        children = data.get('children', [])

        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            for word in word_list:
                if word.lower() in title:
                    word_count[word] = word_count.get(word, 0) + 1

        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no posts match.")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
