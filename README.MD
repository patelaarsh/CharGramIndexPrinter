# CharGramIndexPrinter Homework 1
Convert given corpus data and print index for char grams in each document.

## Data
Given a text file with corpus for test names some-corpus.txt contains 
following data separated by '---'

1) The quick or the brown fox
2) jumped over sally
3) and the brilliant bob fox
4) but not the brown peter bunny

For each term in this sorted order, program outputs, the term on a line by itself. 
On the next line it outputs the number of documents the term appeared in, comma, 
the number of occurrences of the term across all documents, comma, and 
then a list a sequence of pairs in the form (doc_num, character position 
within the document that the term appears at). For example, the entry for _jum might look like:

_jum \
1,1,(1,2)

## Run the Script
usage: CharGramIndexPrinter.py [-h] filename ngram

positional arguments:
  filename    get corpus data
  ngram       get ngram value

options:
  -h, --help  show this help message and exit

Example: python CharGramIndexPrinter.py some-corpus.txt 4
