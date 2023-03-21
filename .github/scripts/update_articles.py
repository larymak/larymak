import requests
import feedparser  # If using RSS


def get_articles():
    rss_url = "https://feedly.com/i/subscription/feed/https://www.freecodecamp.org/news/author/larymak/rss/"
    feed = feedparser.parse(rss_url)

    articles = []
    # Adjust the number to show more or fewer articles
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "url": entry.link,
        })

    return articles


def update_readme(articles):
    readme_file = "README.md"
    article_section_start = "<!-- ARTICLES_START -->"
    article_section_end = "<!-- ARTICLES_END -->"

    with open(readme_file, "r") as f:
        content = f.read()

    new_content = []
    for line in content.split("\n"):
        if line.strip() == article_section_start:
            break
        new_content.append(line)

    new_content.append(article_section_start)
    for article in articles:
        new_content.append(f"- [{article['title']}]({article['url']})")
    new_content.append(article_section_end)

    with open(readme_file, "w") as f:
        f.write("\n".join(new_content))


if __name__ == "__main__":
    articles = get_articles()
    update_readme(articles)
