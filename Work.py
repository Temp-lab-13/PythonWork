from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/<name>/')
def func_name(name):
    print(type(name))
    return f'<h1>Привет</h1>, <p>{name}</p>'

@app.route('/temp/')
def temp():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

