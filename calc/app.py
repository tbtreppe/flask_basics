from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_it():
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def sub_it():
    """Substract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def mult_it(a, b):
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def div_it(a, b):
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)
