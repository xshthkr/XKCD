import requests


def get_current_xkcd():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    data = response.json()
    return data


def print_comic_details(comic_data):
    print("Title:", comic_data['title'])
    print("Comic Number:", comic_data['num'])
    print("Date:", f"{comic_data['month']}/{comic_data['day']}/{comic_data['year']}")
    print("Image URL:", comic_data['img'])
    print("Alt Text:", comic_data['alt'])


def main():
    current_comic = get_current_xkcd()
    print_comic_details(current_comic)


if __name__ == "__main__":
    main()
