import feedparser

blog_rss_url = 'https://v2.velog.io/rss/honeybeat1'
rss_feed = feedparser.parse(blog_rss_url)
MAX_POST_NUM = 10
latest_blog_post_list = ""

for idx, feed in eunmerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_txt = """기본으로 변하지 않을 README.md 값"""
readme_txt = f"{markdown_txt}{latest_blog_post_list}"

with open("README.md",'w',encoding='utf-8') as f:
    f.write(readme_txt)
