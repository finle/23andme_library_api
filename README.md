23andme_library_api

Objective:
==========
The objective of this assignment is to build a console line application with the data that you get from the google books api.
We will be using a simple unauthenticated google books api to get a list of books. And build a library with these books.
Please adhere to good coding practices and code quality.

===
Go ahead and copy paste this link https://www.googleapis.com/books/v1/volumes?q=python on any web browser and see what it returns.
This API can also take additional parameter like https://www.googleapis.com/books/v1/volumes?q=python&maxResults=40
More information about the API can be found here https://developers.google.com/books/docs/v1/reference/volumes/list or by just googling in general.

Requirements:
============
1. The console line app should prompt the user for a search string and based on the input string the app must build the library. Please stick to popular search strings like 'dogs','cats','New York'... etc.
2. The app user must be able to save and persist the book/library data in csv file format.
3. Ability to at least sort the books by price, avg rating, rating count, published date, page count
4. The app should be able to save to and load from a csv file.
5. Bonus points for additional interesting and creative features not listed here. (Nice to see, but not required)

Tests:
============
Please include tests to cover your work.

Usage:
============
To get help run "python3 library_cli.py -h"

usage: library_cli.py [-h] [--search] --output OUTPUT [--sort SORT]
                      [--load LOAD] [--reverse_order]

optional arguments:
  -h, --help       show this help message and exit
  --search         Prompt for search query in GET request
  --output OUTPUT  Name of file to save as, make sure to have permissions to
                   write
  --sort SORT      Choose to sort from following keys: {id, book_title,
                   list_price, avg_rating, ratings_count, published_date}
  --load LOAD      Load from csv file, make sure to have permissions to read
  --reverse_order  Bonus feature: sort by descending order

To append new search results to existing library and save to output csv file:
"python3 library_cli.py --load library.csv --search --output library_append.csv"

The output file is a requirement in the command line
