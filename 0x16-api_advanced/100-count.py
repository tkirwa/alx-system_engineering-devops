import requests


# Function to get the hot articles from a subreddit using Reddit API
def get_hot_articles(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit Keyword Counter"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["children"]
    else:
        return []


# Function to count occurrences of keywords in titles
def count_keywords_in_titles(titles, keywords):
    keyword_count = {keyword: 0 for keyword in keywords}
    for title in titles:
        title_text = title["data"]["title"].lower()
        for keyword in keywords:
            if f" {keyword} " in f" {title_text} ":
                keyword_count[keyword] += 1
    return keyword_count


# Main function to count and print sorted keyword counts
def count_words(subreddit, word_list):
    if not word_list:
        return

    titles = get_hot_articles(subreddit)
    keyword_count = count_keywords_in_titles(titles, word_list)

    sorted_keywords = sorted(
        keyword_count.items(),
        key=lambda item: (-item[1], item[0])
    )

    for keyword, count in sorted_keywords:
        print(f"{keyword}: {count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [word.lower() for word in sys.argv[2:]]
        count_words(subreddit, keywords)
