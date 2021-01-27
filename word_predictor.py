# Name: Word Predictor
# Purpose: Reads a corpus, extracts all ngrams and prompts user for n-1 words in order to predict the n'th word

import sys


def main(argv):

    # Check input
    if len(argv) != 3:
        print(f"Incorrent argument count. Usage: {argv[0]} file integer\n", file=sys.stderr)
        sys.exit(1)

    try:
        with open(argv[1]) as infile:
            text = infile.read()

    except FileNotFoundError:
        print(f"Could not open file. Usage: {argv[0]} file integer\n", file=sys.stderr)
        sys.exit(2)

    try:
        n = int(argv[2])
        
    except ValueError:
        print(f"Incorrect argument type. Usage: {argv[0]} file integer\n", file=sys.stderr)
        sys.exit(3)

    # Store ngrams of text into a dictionary
    ngrams = extract_ngrams(text, n)
 
    # dict.get() methods returns value of key, here used for sorting by frequency
    # sorted_ngrams = list of dict keys sorted based on values in descending order
    sorted_ngrams = sorted(ngrams, key=ngrams.get, reverse=True)

    # Will repeat until user presses ENTER
    x = True
    while x:
        words = prompt_words(n)
        if words == None:
            x = False
            break
        check_sequence(sorted_ngrams, words)

        
# Function takes as input text and int n
# returns a dict s.t. keys are n-grams
# and values are ngram frequencies
def extract_ngrams(text, n):
    ngrams = dict()
    text = text.split()

    # stop iteration at n'th to last word
    # since last n words = last n-gram
    for i in range(len(text)-n):
        words = tuple(text[i:i+n])
        if words in ngrams:
            ngrams[words] = ngrams[words] + 1
        else:
            ngrams[words] = 1

    return ngrams

# Prompts user for n-1 words, returns words as list
# If user presses ENTER, returns nothing
def prompt_words(n):

    string_words = input(f"Write {n-1} words, I'll tell you what the next one should be [press ENTER to escape]\n")
    if string_words == "":
        return None

    words = string_words.split()
    if len(words) != n-1:
        print(f"Wrong input. Write {n-1} words, otherwise press ENTER\n")
        return prompt_words(n)
    else:
        return words

# Takes as input sorted list of ngrams and user's words list
# Checks if user's input corresponds to first n-1 words of ngram
# if yes => prints the n'th word from ngrams
# otherwise prints no clue
def check_sequence(sorted_ngrams, words):

    for ngram in sorted_ngrams:

        # Assume ngram == user input
        # iterate over ngram comparing with user input
        # if input corresponds to ngram print last token
        same = True
        for i in range(len(words)):
            if ngram[i] != words[i]:
                same = False
        if same:
            return print(f"[ {ngram[-1]} ]")

    return print("no clue")


if __name__ == "__main__":
    main(sys.argv)
