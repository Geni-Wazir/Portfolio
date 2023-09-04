from flask import Flask, render_template, url_for, redirect
import feedparser





app = Flask(__name__)    
app.config['SECRET_KEY'] = '3fd5f6f457adc67ee57d46373dc1b62d7d26a543'




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
        post['image'] = entry.summary[entry.summary.index("<img src=")+10:entry.summary.index(' width=')-1]
        post['summary'] = entry.summary[entry.summary.index('class="medium-feed-snippet')+28:entry.summary.index('</p><p class="medium-feed-link"')]
        blogs.append(post)
    return render_template('blogs.html', blogs=blogs)

@app.route('/connect')
def connect():
    return render_template('connect.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
