import os
from flask import Flask
from flask import request
from werkzeug import secure_filename


def save(file):
    filename = secure_filename(file.filename)
    save_path = os.path.join(os.getcwd(), filename)
    file.save(save_path)
    return save_path

app = Flask(__name__)


@app.route("/", methods=["POST"])
def post():
    file = request.files['file']
    return "Uploaded. compressed file. path: {}".format(save(file))


def run_server():
    print ("CWD: {}".format(os.getcwd()))
    debug = False
    if os.environ.get("DEBUG", "no") == "yes":
        debug = True

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=debug,
        threaded=True
    )

if __name__ == "__main__":
    run_server()
