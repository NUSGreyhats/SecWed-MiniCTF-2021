from flask import Flask, g
from constants import FLAG
import ctypes
import sys
from html import escape
import multiprocessing as mp

app = Flask(__name__)

@app.before_request
def store():
    g.shared = mp.Manager().dict()

@app.route('/')
def index():
    with open(__file__) as f:
        return f"<pre>{f.read()}</pre>"


@app.route('/<path:path>')
def a(path):
    p = mp.Process(target=func, args=(path, g.shared))
    p.start()
    p.join()

    if p.exitcode != 0:
        p.close()
        return f"<pre>{FLAG}</pre>"
    else:
        p.close()
        return f"<pre>{sys.version}</pre><br/><pre>{g.shared['result']}</pre>"

def func(path, shared):
    try: 
        n = int(path)
        no = ctypes.c_double.from_param(n)
        shared['result'] = f'<pre>{escape(repr(no))}<pre>'
    except Exception as e:
        print(e)
        shared['result'] = "Not a float"


def sig_handler(signum, frame):
    return FLAG


if __name__ == '__main__':
    mp.freeze_support()
    app.run(debug=True)
