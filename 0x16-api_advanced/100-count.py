#!/usr/bin/python3
"""
Module for counting occurrences of keywords in Reddit hot post titles.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive function that queries the Reddit API, parses the title of
    all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces).

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of keywords to search for.
        after (str, optional): The 'after' parameter for pagination.
          Defaults to None.
        counts (dict, optional): A dictionary to store word counts.
          Defaults to None.
    """
    # If 'counts' is None, initialize it as an empty dictionary
    if counts is None:
        counts = {}

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
            # If there are no more posts, print the counts in the specified
            #  format
            print_counts(counts, word_list)
            return

        # Process the posts and update the word counts
        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    counts[word.lower()] = counts.get(word.lower(), 0) + count

        # Get the 'after' parameter for pagination
        after = data['data']['after']

        # Recursively call the function with the updated parameters
        #  for the next page
        count_words(subreddit, word_list, after, counts)
    else:
        # If the subreddit is invalid or an error occurs, print nothing
        return


def print_counts(counts, word_list):
    """Prints the word counts in the specified format.

    Args:
        counts (dict): A dictionary containing word counts.
        word_list (list): The list of keywords to search for.
    """
    # Sort the counts in descending order by the count and ascending
    #  order by the word
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1],
                                                             item[0]))

    # Print the counts for the given keywords
    for word, count in sorted_counts:
        if word in word_list:
            print(f"{word}: {count}")


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
