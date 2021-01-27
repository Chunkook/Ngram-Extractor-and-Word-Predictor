# Name: Ngram
# Purpose: Reads a corpus and extracts all ngrams in order of frequency

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

    # Store ngrams from text into a dictionary
    ngrams = extract_ngrams(text, n)
 
    # dict.get() methods returns value of key, here used for sorting by frequency
    # sorted_ngrams = list of dict keys sorted based on values in descending order
    sorted_ngrams = sorted(ngrams, key=ngrams.get, reverse=True)

    # Print ngram and its value from ngram dictionary
    # format tuple as string where ' ' is separator
    # .ljust(int) justifies whitespace after string
    for ngram in sorted_ngrams:
        print(f"{' '.join([str(word) for word in ngram]).ljust(n*10)} {ngrams[ngram]}", file=sys.stdout)


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


if __name__ == "__main__":
    main(sys.argv)
