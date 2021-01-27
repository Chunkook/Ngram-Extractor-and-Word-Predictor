## Ngram Extractor

**Description:**

Program takes as input a text file and extracts all ngram specified by user ordered by frequency.

**Usage:**

`python3 ngram_extractor.py <file.txt> <integer ngrams>`

*Example:* `python3 ngram_extractor.py sample.txt 4` will extract all 4-grams from sample.txt in order of frequency.


## Word Predictor

**Description:**

Program takes as input a text file and extracts all ngram specified by user, followed by prompting a user to enter n-1 words in order to propose what the n'th word will be.

**Usage:**

`python3 word_predictor.py <file.txt> <integer ngrams>`

*Example:* `python3 word_predictor.py sample.txt 3` will extract all 3-grams, prompt the user to input 2 words and attempt to return the third if there exists a 3-gram with the 2 words the user inputted.
