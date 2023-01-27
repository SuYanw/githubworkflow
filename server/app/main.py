import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    
    my_keys = {
        'DB_HOST',
        'DB_USER',
        'DB_PASS'
    }

    if(my_keys <= os.environ.keys()):

        return f""" DB_HOST: {os.environ['DB_HOST']}<br />
                    DB_USER: {os.environ['DB_USER']}<br />
                    DB_PASS: {os.environ['DB_PASS']}<br />
                    DB_DB: {os.environ['DB_BASE']}<br />
                    DB_PORT: {os.environ['DB_PORT']}<br />
                    """

    return "Hello, World!<br/>Here didn't have a special keys<br/>Try again later"

if __name__ == '__main__':
    app.run(debug=True)