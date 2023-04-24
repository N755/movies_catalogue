from flask import Flask, render_template,request


app = Flask(__name__)

app.secret_key = 'secret'


@app.route('/')
def homepage():
    movies = []
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)