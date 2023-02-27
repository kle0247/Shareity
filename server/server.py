from flask import Flask
from config import Configuration

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)