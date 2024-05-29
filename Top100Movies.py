import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
print(soup)

titles_list = []
titles = soup.find_all(name="h3", class_="title")
print(titles)

# Get the text from the element h3, aka the title:
for tag in titles:
    title_txt = tag.getText()
    titles_list.append(title_txt)

# Reverse the list using list slicing:
titles_list = titles_list[::-1]
print(titles_list)

# Create a txt file, and write each element of a list in a new line:
file = open('top100movies.txt', 'w+', encoding='utf-8')
# # Idea from: https://stackoverflow.com/questions/7138686/how-to-write-a-list-to-a-file-with-newlines-in-python3
for item in titles_list:
    file.write(f"\n{item}")
