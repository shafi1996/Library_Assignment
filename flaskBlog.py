from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
        {
            'author': 'Muhammed',
            'title' : 'Intro to Python',
            'isbn': 'ISB:3457',
            'release_date' : 'April 20, 2019'
        },
        {
            'author': 'Johnathan',
            'title' : 'Intro to C++',
            'isbn': 'ISB:45627',
            'release_date' : 'April 20, 2020'
        }
]

@app.route("/")
@app.route("/Home")
def hello_world():
    return render_template('home.html',posts=posts)




@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
