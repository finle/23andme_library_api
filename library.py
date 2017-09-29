import argparse
import json
import requests


parser = argparse.ArgumentParser()
parser.add_argument("--search", action="store_true")
args = parser.parse_args()


if __name__ == "__main__":

    if args.search:
        search_string = input("Please enter search string: ")

    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=kevin")
    print(r.text)