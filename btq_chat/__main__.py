from .parse_args import *
from .scraper import *


def main():
    args = parse_args()
    prompt = args["prompt"]
    response = scrape(prompt)
    print()
    print(response)


if __name__ == "__main__":
    main()
