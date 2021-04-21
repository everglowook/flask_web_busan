from flask import Flask , render_template, request, redirect
from data import Articles
import pymysql

app = Flask(__name__) 

app.debug = True 

db = pymysql.connect(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db = 'busan'
)
cursor = db.cursor()

@app.route('/', methods=['GET']) 
def index():
    # return "Hello World" 
    return render_template("index.html", data ="KIM")

@app.route('/about')
def about():
    return render_template("about.html", Hello = "Gary Kim")
@app.route('/articles')
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    # articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = topics)

@app.route('/article/<int:id>')
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'. format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods=["GET", "POST"])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title,desc,author]

        print(request.form['author'])


        cursor.execute(sql, input_data)
        db.commit()
        # db.close()
        print(cursor.rowcount)
        return redirect("/articles") 

    # return "<h1>글쓰기 페이지</h1>"
    else:
        return render_template("add_articles.html")


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    # sql = 'DELETE FROM topic WHERE id = %s;'
    # id = '[]id'
    # cursor.execute(sql, id)
    sql = 'delete from topic where id = {};' .format(id)
    cursor.execute(sql)
    db.commit()

    return redirect("/articles")

@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        return "Success"
    
    else:
        return render_template("edit_article.html")
    



if __name__ == '__main__':
    app.run() 