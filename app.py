
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World! This is your endpoint.'

if __name__ == '__main__':
    app.run(port=5000)
