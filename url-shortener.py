from base64 import b64encode
from hashlib import blake2b
import random
import re
import json

# URL validation regex
regex = re.compile(
        r'^(?:http)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
DIGEST_SIZE = 9  # 72 bits of entropy.
shortened = {}


def url_valid(url):
    """Validates a URL by parsing it with a regular expression.

    Parameters:
    url - string representing a URL to be validated.

    Return values:
    Boolean, indicating the validity of the URL.
    """
    return re.match(regex, url) is not None


def shorten(url):
    """Shortens a URL by generating a 9-byte hash, and then
    converting it to a 12-character long base 64 URL-friendly string.

    Parameters:
    url - the URL to be shortened.

    Return values:
    String, the unique shortened URL, acting as a key for the entered long URL.
    """
    url_hash = blake2b(str.encode(url), digest_size=DIGEST_SIZE)

    while url_hash in shortened:
        url += str(random.randint(0, 9))
        url_hash = blake2b(str.encode(url), digest_size=DIGEST_SIZE)

    b64 = b64encode(url_hash.digest(), altchars=b'-_')
    return b64.decode('utf-8')


def main():
    while True:
        print("URL Shortener")
        print("1. Shorten URL")
        print("2. Retrieve original URL")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter the URL to be shortened: ")

            if url[:4] != 'http':
                url = 'http://' + url

            if not url_valid(url):
                print("Provided URL is not valid.")
                continue

            shortened_url = shorten(url)
            shortened[shortened_url] = url
            print(f"Shortened URL: {shortened_url}")

        elif choice == '2':
            alias = input("Enter the shortened URL: ")

            if alias not in shortened:
                print("Unknown alias.")
            else:
                print(f"Original URL: {shortened[alias]}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
