import collections

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

my_cookies = {
    "name": "pkbRem",
    "value": "%7B%22uid%22%3A3019715%2C%22username%22%3A%22PapaGuss%22%2C%22rem%22%3A%2212ffc280f4b7776a5e69cc5ccfa45335%22%2C%22tries%22%3A0%7D",
}

base_url = "https://pikabu.ru/new/subs?page="


def pikaboo_parse(headers):
    session = requests.Session()
    session.cookies.set(**my_cookies)

    all_tags = []
    number_of_stories = 0
    iteration = 0
    while number_of_stories != 100:
        iteration += 1
        response = session.get(base_url + str(iteration), headers=headers)
        page = BeautifulSoup(response.content, "html.parser")
        stories = page.find("div", attrs="stories-feed__container").find_all("article")
        stories.pop()  # delete advertisement post
        number_of_stories += len(stories)

        for story in stories:
            title, key_words = parse_story(story)
            print(title)
            all_tags.extend(key_words)

    tags = collections.Counter()
    for tag in all_tags:
        tags[tag] += 1

    print("\nTotal number of tags:", len(tags))
    with open("10 most common tags.txt", "wb") as output:
        line = ""
        for pair in tags.most_common(10):
            line += f"{pair[0]}\t{pair[1]}\n"
        output.write(bytes(line.encode()))


def parse_story(story):
    title = story.find("h2", attrs="story__title").find("a").text
    tags = story.find("div", attrs="story__tags tags").find_all("a")
    return title, [tag.text.replace("\xa0", "") for tag in tags]


if __name__ == "__main__":
    pikaboo_parse(headers)
