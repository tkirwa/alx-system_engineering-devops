import requests


def count_words(subreddit, word_list, after=None, counts={}):
    # Set the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent header
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    # Add 'after' parameter if it exists
    params = {'after': after} if after else {}
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        # Parse the JSON response from Reddit
        data = response.json()
        posts = data['data']['children']
        # If there are no more posts, sort and print the word counts
        if not posts:
            sorted_counts = sorted(counts.items(), key=lambda item: (-item[1],
                                                                     item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
        else:
            # Get the 'after' parameter for the next request
            after = data['data']['after']
            # Count occurrences of keywords in each article title
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if f" {word.lower()} " in f" {title} ":
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            # Recursive call with the updated 'after' parameter and counts
            count_words(subreddit, word_list, after, counts)
    else:
        # If the API request is not successful or no posts match, print nothing
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
