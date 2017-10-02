import argparse
import pandas as pd
import requests


class Library(object):

    def __init__(self, query=None, key=None, reverse=False):

        self.key = key
        self.reverse = reverse
        self.query = query
        self.list_book_objects = []

    def search(self, query):

        """
        :param query: query string
        :return: list of dictionary of book objects
        """
        params = {"q": query}
        try:
            r = requests.get("https://www.googleapis.com/books/v1/volumes", params=params)
        except Exception as e:
            print(e)
        books_json = r.json()["items"]

        # handle case where books have no price, set amount to None
        # convert publishedDate to datetime
        # handle case for averageRating and ratingsCount
        # replace commas from title to prevent csv parsing when loading
        for book in books_json:

            book["saleInfo"].setdefault("listPrice", {"amount": 0.0})
            book["volumeInfo"]["publishedDate"] = str(pd.to_datetime(book["volumeInfo"]["publishedDate"]))
            book["volumeInfo"].setdefault("averageRating", 0.0)
            book["volumeInfo"].setdefault("ratingsCount", 0.0)
            book["volumeInfo"]["title"] = book["volumeInfo"]["title"].replace(",", "")

        return books_json

    def sort_list_book_objects(self, key=None, reverse=False):

        """
        :param item_list: list of dictionary book objects
        :param key: string key to sort on
        :param reverse: sort by ascending or descending
        """
        try:
            self.list_book_objects = sorted(self.list_book_objects, key=lambda x: x[key], reverse=reverse)
        except Exception as e:
            print(e)


    def query_to_list_book_objects(self, query):

        """
        :param query: query string
        :return: None
        """
        list_query_books = self.search(query)
        for book in list_query_books:

            self.list_book_objects.append({
                "id": book["id"],
                "book_title": book["volumeInfo"]["title"],
                "list_price": book["saleInfo"]["listPrice"]["amount"],
                "avg_rating": book["volumeInfo"]["averageRating"],
                "ratings_count": book["volumeInfo"]["ratingsCount"],
                "published_date": book["volumeInfo"]["publishedDate"]
            })

    def save_to_csv(self, csv_file_location):

        # each row will be id, book_title, list_price, avg_rating, ratings_count, published_date
        try:
            with open(csv_file_location, "w") as csv_file:

                for book in self.list_book_objects:
                    csv_file.write("{id},{book_title},{list_price},{avg_rating},{ratings_count},{published_date}\n".format(**book))
        except Exception as e:
            print(e)

    def load_to_list_book_objects(self, csv_file_location):

        """
        :param csv_file_location: location of csv file
        :return: None
        """
        try:
            with open(csv_file_location) as csv_file:
                for line in csv_file:
                    line = line.strip("\n").split(",")
                    self.list_book_objects.append({
                        "id": line[0],
                        "book_title": line[1],
                        "list_price": float(line[2]),
                        "avg_rating": float(line[3]),
                        "ratings_count": line[4],
                        "published_date": line[5]
                    })
        except Exception as e:
            print(e)




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--search",
                        action="store_true",
                        help="Prompt for search query in GET request")
    parser.add_argument("--output",
                        action="store",
                        required=True,
                        help="Name of file to save as, make sure to have permissions to write")
    parser.add_argument("--sort",
                        action="store",
                        help="Choose to sort from following keys: {id, book_title, list_price, avg_rating, ratings_count, published_date}")
    parser.add_argument("--load",
                        action="store",
                        help="Load from csv file, make sure to have permissions to read")
    parser.add_argument("--reverse_order",
                        action="store_true",
                        help="Bonus feature: sort by descending order")
    args = parser.parse_args()

    init_library = Library()

    if args.load:
        init_library.load_to_list_book_objects(args.load)

    if args.search:
        query = input("Please enter search string: ")
        init_library.query_to_list_book_objects(query)

    if args.sort:
        if args.sort.lower() not in ["id", "book_title", "list_price", "avg_rating", "ratings_count", "published_date"]:
            raise Exception("Please choose a valid key")
        else:
            init_library.sort_list_book_objects(key=args.sort,reverse=args.reverse_order)

    if args.output:
        init_library.save_to_csv(args.output)
