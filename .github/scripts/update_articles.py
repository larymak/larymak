import requests
import feedparser  # If using RSS


def get_articles():
    rss_url = "https://www.freecodecamp.org/news/author/larymak/rss/"
    feed = feedparser.parse(rss_url)

    articles = []
    # Adjust the number to show more or fewer articles
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "url": entry.link,
        })

    return articles
# def get_articles():
#     rss_url = "https://www.freecodecamp.org/news/author/larymak/rss/"
#     feed = feedparser.parse(rss_url)

#     # Check if the feed title is being fetched
#     print(f"Feed title: {feed.feed.title}")
#     # Check the number of entries in the feed
#     print(f"Total entries: {len(feed.entries)}")

#     articles = []
#     # Adjust the number to show more or fewer articles
#     for entry in feed.entries[:5]:
#         articles.append({
#             "title": entry.title,
#             "url": entry.link,
#         })

#     return articles


def update_readme(articles):
    placeholder = "<!-- ARTICLES:START -->\n\n<!-- ARTICLES:END -->"

    article_md_list = []
    for article in articles:
        article_md_list.append(f'- [{article["title"]}]({article["url"]})')

    articles_md = "\n".join(article_md_list)

    with open("README.md", "r", encoding='utf-8') as readme:  # Set encoding to 'utf-8'
        content = readme.read()

    new_content = content.replace(
        placeholder, f"<!-- ARTICLES:START -->\n\n{articles_md}\n\n<!-- ARTICLES:END -->")

    with open("README.md", "w", encoding='utf-8') as readme:  # Set encoding to 'utf-8'
        readme.write(new_content)


if __name__ == "__main__":
    articles = get_articles()
    print(articles)
    update_readme(articles)


# if __name__ == "__main__":
#     articles = get_articles()
#     print(articles)  # Print the fetched articles
#     update_readme(articles)
