# dictionary-api-python-flask/app.py
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from model.dbHandler import match_exact
from model.dbHandler import match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    return jsonify(response)

@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    words = request.args.getlist("word")
    if not words:
        return jsonify({"stats":"error","words":words,"data":"word not found"})
    # initialize the response...
    response = {"words":[]}
    for word in words:
        definitions = match_exact(word)
        if definitions:
            response['words'].append({"status":"success","word":word,"data":definitions}) 
        else:
            definitions = match_like(word)
            if definitions:
                response['words'].append({"status":"partical","word":word,"data":definitions}) 
            else:
                response["words"].append({"status":"error","word":word,"data":"word not found"})
    return jsonify(response)




    if not word:
        return jsonify({"status":"error", "data":"word not found"})
    definition = match_exact(word)
    if definition:
        return jsonify({"status":"success", "data":definition})
    definitions = match_like(word)
    if definitions:
        return jsonify({"status":"partial", "data":definitions})
    else:
        return jsonify({"status":"error", "data":"word not found"})

if __name__ == "__main__":
    app.run()
