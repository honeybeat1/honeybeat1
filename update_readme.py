import feedparser

blog_rss_url = 'https://v2.velog.io/rss/honeybeat1'
rss_feed = feedparser.parse(blog_rss_url)
MAX_POST_NUM = 10
latest_blog_post_list = ""
MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_txt = """
![header](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=200&section=header&text=dahyun%20chung%20☁️&fontSize=70)

<div align="center">
  
![honeybeat1's GitHub stats](https://github-readme-stats.vercel.app/api?username=honeybeat1&show_icons=true&theme=nord)
</div>

✍️ Latest velog Post

"""

readme_txt = f"{markdown_txt}{latest_blog_post_list}"

with open("README.md",'w',encoding='utf-8') as f:
    f.write(readme_txt)
