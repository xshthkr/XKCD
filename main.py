import requests

README_FILE = "README.md"
MONTHS = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


def get_current_xkcd():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    data = response.json()
    return data


def generate_readme(comic_data):
    readme_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1 style="text-align:center;"><a href="https://xkcd.com">XKCD</a></h1>
    <p style="text-align:center;">Dynamically generated every midnight UTC</p>
    <hr>
    <div style="text-align:center;">
        <h3><strong>{comic_data['title']}</strong></h3>
        <p>#{comic_data['num']}</p>
        <p>{MONTHS[int(comic_data['month'])]} {comic_data['day']}, {comic_data['year']}</p>
        <img src="{comic_data['img']}" alt="XKCD Comic" style="display:block;margin:auto;">
        <p><em>{comic_data['alt']}</em></p>
    </div>
</body>
</html>
"""

    with open(README_FILE, "w") as readme_file:
        readme_file.write(readme_content)


def main():
    current_comic = get_current_xkcd()
    generate_readme(current_comic)
    print(f"README.md updated with the current XKCD comic ({current_comic['num']})")


if __name__ == "__main__":
    main()
