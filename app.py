from flask import Flask , render_template


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
    return render_template("articles.html", hello = "Gary Kim")

if __name__ == '__main__':
    app.run() 