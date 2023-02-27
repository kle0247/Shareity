from flask import Flask
from bll.searchNames import search_names
import pdb

app = Flask(__name__)

@app.route('/')
def index():
    url = search_names('pets')
    pdb.set_trace()
    return url

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)