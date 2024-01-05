from flask import Flask, render_template
import feedparser



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
        post['summary'] = entry.summary[entry.summary.index('<p>')+3:entry.summary.index('<p>')+453] + "...."
        blogs.append(post)
    return render_template('blogs.html', blogs=blogs)



if __name__ == "__main__":
    app.run(debug=False, port=5000)
