from flask import Flask , render_template
from data import Articles

app = Flask(__name__) 

app.debug = True 

@app.route('/', methods=['GET']) 
def index():
    # return "Hello World" 
    return render_template("index.html", data ="KIM")

@app.route('/about')
def about():
    return render_template("about.html", Hello = "Gary Kim")
@app.route('/articles')
def articles():
    articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = articles)

@app.route('/article/<int:id>')
def article(id):
    articles = Articles()
    article = articles[id-1]
    print(articles[id-1])
    return render_template("article.html", article = article)

if __name__ == '__main__':
    app.run() 