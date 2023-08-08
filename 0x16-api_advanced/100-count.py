#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    # Set the URL for the Reddit API with the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    # Set the User-Agent header for the request
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Set the parameters for the API request
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        # Parse the JSON response from the API
        results = response.json()
        # Raise an exception if the response status code is 404 (Not Found)
        if response.status_code == 404:
            raise Exception
    except Exception:
        # If there's an exception (invalid subreddit or other error),
        # print an empty line and return
        print("")
        return

    # Extract the necessary data from the API response
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    # Count occurrences of keywords in the post titles
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    # If there are no more posts, print the word counts in the specified format
    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        # If there are more posts, make a recursive call to continue
        #  querying the API
        count_words(subreddit, word_list, instances, after, count)
