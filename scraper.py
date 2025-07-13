import requests
from bs4 import BeautifulSoup
import os

# Fetch the articles page
url = "http://www.paulgraham.com/articles.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract article links
articles = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith('.html') and not href.startswith('http'):
        full_url = f"http://www.paulgraham.com/{href}"
        articles.append(full_url)

# Scrape each article
for article_url in articles:
    try:
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        
        # Extract title and content
        title = article_soup.find('title').text
        content = article_soup.find('font', {'face': 'verdana'}).text
        
        # Save as markdown
        filename = title.replace(' ', '_').lower() + '.md'
        with open(f"paulgraham_articles/{filename}", 'w') as f:
            f.write(f"# {title}\n\n{content}")
    except Exception as e:
        print(f"Failed to scrape {article_url}: {e}")