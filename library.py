import argparse
import json
import requests


parser = argparse.ArgumentParser()
parser.add_argument("--search", action="store_true")
args = parser.parse_args()


if __name__ == "__main__":

    params = {'q' : None}

    if args.search:
        params['q'] = input("Please enter search string: ")

    #r = requests.post("https://www.googleapis.com/books/v1/volumes?q=kevin")
    r = requests.get("https://www.googleapis.com/books/v1/volumes", params=params)
    print(r.text)