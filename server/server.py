from flask import Flask
from bll.searchNames import search_names
import pdb
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return 'hello world'

@app.route('/search/<term>')
def search(term):
    return search_names(term)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)