import requests

README_FILE = "README.md"


def get_current_xkcd():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    data = response.json()
    return data


def generate_readme(comic_data):
    readme_content = f"""
        # Current XKCD Comic
        
        Title: {comic_data['title']}  
        Comic Number: {comic_data['num']}  
        Date: {comic_data['month']}/{comic_data['day']}/{comic_data['year']}  
        
        ---
        
        ![XKCD Comic]( {comic_data['img']} )  
        
        {comic_data['alt']}
    """
    with open(README_FILE, "w") as readme_file:
        readme_file.write(readme_content)


def main():
    current_comic = get_current_xkcd()
    generate_readme(current_comic)
    print(f"README.md updated with the current XKCD comic ({current_comic['num']})")


if __name__ == "__main__":
    main()
