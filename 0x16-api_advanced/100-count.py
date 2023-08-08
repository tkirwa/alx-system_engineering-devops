#!/usr/bin/python3
# Import necessary modules
from requests import get
from sys import argv

# Initialize the list to store hot article titles and the after parameter
hotlist = []
after = None


# Function to count occurrences of words from word_list in hotlist
def count_all(hotlist, word_list):
    # Create a dictionary to store word counts
    count_dic = {word.lower(): 0 for word in word_list}
    for title in hotlist:
        words = title.split(' ')
        for word in words:
            if count_dic.get(word) is not None:
                count_dic[word] += 1

    # Sort and print word counts in descending order
    for key in sorted(count_dic, key=count_dic.get, reverse=True):
        if count_dic.get(key):
            for thing in word_list:
                if key == thing.lower():
                    print("{}: {}".format(thing, count_dic[key]))


# Recursive function to count words in titles of hot articles
def count_words(subreddit, word_list):
    global hotlist
    global after

    # Set User-Agent for the API request
    head = {'User-Agent': 'Dan Kazam'}

    # Construct the API URL with or without the 'after' parameter
    if after:
        count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=head).json().get('data')
    else:
        count = get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=head).json().get('data')

    # Add lowercase titles to hotlist
    hotlist += [dic.get('data').get('title').lower()
                for dic in count.get('children')]
    after = count.get('after')

    # If there are more articles, recurse; otherwise, count occurrences
    if after:
        return count_words(subreddit, word_list)
    return count_all(hotlist, word_list)


# Main code block
if __name__ == "__main__":
    # Call count_words with subreddit and word_list from command-line arguments
    count_words(argv[1], argv[2].split(' '))
