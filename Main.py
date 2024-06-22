import newspaper
import feedparser

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url):
    for entry in feed.entries:
        article = newspaper.Article(entry.link)
        
         article.download()
         article.parse()

          articles.append({
              'title': article.title,
    #          'author': article.authors,
    #          'publish_date': article.publish_date,
    #          'content': article.text
    #      })
    #  return articles

