from bs4 import BeautifulSoup
import requests
# Step 1: Save a webpage into html text
response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text

# Step 2: create a soup object with the webpage as an argument
soup = BeautifulSoup(yc_webpage, "html.parser")

# Select every element with a class of titleline:
title_list = soup.select(selector=".titleline")
print(title_list)

article_title_list = []
article_links_list = []
article_upvote_list = []

# Find every element with a class of title line
title_list_2 = soup.find_all(class_="titleline")
print(title_list_2)

for tag in title_list_2:
    article_title = tag.find(name="a").getText()
    article_title_list.append(article_title)
    article_link = tag.find(name="a").get("href")
    article_links_list.append(article_link)

score_list = soup.find_all(class_="score", name="span")
for score in score_list:
    article_upvotes = score.getText()
    article_upvotes = article_upvotes.split(" ")[0]
    article_upvote_list.append(article_upvotes)

# # # # Remember, the get text is used to get the text stored as an element bewtween the tags
print(article_title_list)
print(article_links_list)
print(article_upvote_list)

# Convert the list to Integer, so we can use the max function:
converted_list_int = list(map(int, article_upvote_list))
# Use max function:
most_upvoted = max(converted_list_int)
# Dont forget to convert back to str to search for index
index = article_upvote_list.index(str(most_upvoted))
print(index)

# Format the returns
most_upvoted_article = f" Title:{article_title_list[index]}, Link:{article_links_list[index]}, Upvotes:{article_upvote_list[index]}"
print(most_upvoted_article)


