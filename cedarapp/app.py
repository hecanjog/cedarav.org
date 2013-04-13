from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    foo = 'bar'
    return render_template('index.html', foo=foo)

if __name__ == '__main__':
    app.run(debug=True)
