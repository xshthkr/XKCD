import requests
import subprocess

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
<h1 align="center"><a href="https://xkcd.com">XKCD</a></h1>
<p align="center"><i>Dynamically updated and generated every midnight UTC</i></p>
<hr>
<div align="center">
    <h3><strong>{comic_data['title']}</strong></h3>
    <p>#{comic_data['num']}</p>
    <p>{MONTHS[int(comic_data['month'])]} {comic_data['day']}, {comic_data['year']}</p>
    <img src="{comic_data['img']}">
    <br></br>
    <p><i>{comic_data['alt']}</i></p>
</div>
"""

    with open(README_FILE, "w") as readme_file:
        readme_file.write(readme_content)


def main():
    current_comic = get_current_xkcd()
    generate_readme(current_comic)
    print(f"README.md updated with the current XKCD comic ({current_comic['num']})")

    # Add README.md to the staging area
    subprocess.run(["git", "add", "README.md"])

    # Commit changes
    commit_message = f"Update README.md with XKCD comic {current_comic['num']}"
    subprocess.run(["git", "commit", "-m", f"updated README.md with {current_comic['num']}"])

    # Push changes to the remote repository
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    main()
