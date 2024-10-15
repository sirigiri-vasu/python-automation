import requests
from bs4 import BeautifulSoup


def main():
    url = "https://realpython.github.io/fake-jobs/"
    res = requests.get(url)
    s = BeautifulSoup(res.content, 'html.parser')
    results = s.find(id="ResultsContainer")
    titles = results.find_all('h2', class_="title is-5")

    for item in titles:
        print(item.text)


if __name__ == "__main__":
    main()




