from flask import Flask

name = 'main'

app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page'

if name == 'main':
    app.run(debug=True)