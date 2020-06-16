# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def addition():
    """add 'a' and 'b'"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = add(a, b)
    return f"Answer: {str(answer)}"


@app.route("/subtract")
def subtract():
    """subtract 'a' and 'b'"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = sub(a, b)
    return f"Answer: {str(answer)}"


@app.route("/multiply")
def multiply():
    """multiply 'a' and 'b'"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = mult(a, b)
    return f"Answer: {str(answer)}"


@app.route("/divide")
def divide():
    """divide 'a' and 'b'"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = div(a, b)
    return f"Answer: {str(answer)}"


# Further Study

"""Dictionary to map operation names"""
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route("/math/<calc>")
def calculation(calc):
    """perform calc operations on 'a' and 'b'"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = operators[calc](a, b)
    return f"Answer: {str(answer)}"
