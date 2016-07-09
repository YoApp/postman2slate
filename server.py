import json
from dotmap import DotMap
from flask import Flask, request, render_template, render_template_string
import os

app = Flask(__name__)


@app.route("/process", methods=['POST'])
def route_process():
    postman_collection_file = request.files.get('collection')
    postman_collection_string = postman_collection_file.read()

    postman_collection_string = render_template_string(postman_collection_string, BASE_URL=os.environ.get('BASE_URL'))

    postman_collection_dict = json.loads(postman_collection_string)

    postman_collection = DotMap(postman_collection_dict)

    return render_template('index.html.md', collection=postman_collection)


@app.template_filter('postman_url')
def postman_url(obj):
    if type(obj) == unicode:
        return obj

    return obj.raw


if __name__ == "__main__":

    app.run()