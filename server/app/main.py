import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    
    out_str = []
    for kvl  in os.environ:
        out_str.append(f"{kvl}={os.environ.get(kvl)} <br/>")
        
    return out_str

if __name__ == '__main__':
    app.run(debug=True)