#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """ A function that queries the Reddit API, parses the titles of all
      hot articles,
    and prints a sorted count of given keywords (case-insensitive,
      delimited by spaces).
    'Javascript' should count as 'javascript', but 'java' should not.
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    # Initialize the word_dict if it's empty
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    # If the 'after' parameter is None, we have reached the end of recursion
    if after is None:
        # Sort the word_dict by count (descending) and then by word (ascending)
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        # Print the sorted count for each keyword with occurrences...
        #  greater than 0
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    # Build the URL for the Reddit API request
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    # Check if the API request was successful (status code 200)
    if response.status_code != 200:
        return None

    try:
        # Parse the JSON response to get the list of hot articles and...
        #  the 'after' parameter
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']

        # Count occurrences of keywords in each article title
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    # Continue the recursion with the new 'after' parameter
    count_words(subreddit, word_list, aft, word_dict)
