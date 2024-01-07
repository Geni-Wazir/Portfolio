from flask import Flask, render_template
import feedparser
import re



app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext


@app.route('/blogs')
def blogs():
    blogs = []
    url = "https://medium.com/feed/@crazycoolbrother"
    feed = feedparser.parse(url)
    for entry in feed.entries:
        post={}
        post['title'] = entry.title
        post['url'] = entry.link[:entry.link.index("?source=rss")]
        post['date'] = entry.published[5:16]
        post['image'] = entry.summary[entry.summary.index("https://cdn-images-1.medium.com"):entry.summary.index(' /')-1]
        post['summary'] = cleanhtml(entry.summary[entry.summary.index('<p>')+3:entry.summary.index('<p>')+500]) + "<strong>......</strong>"
        blogs.append(post)
    return render_template('blogs.html', blogs=blogs)



if __name__ == "__main__":
    app.run(debug=False, port=5000)
