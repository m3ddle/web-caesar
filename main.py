# TODO: Make this work with vig encrypt as well

from flask import Flask, request
import caesar

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
  <head>
    <style>
      form {{
        background-color: #eee;
        padding: 20px;
        margin: 0 auto;
        width: 540px;
        font: 16px sans-serif;
        border-radius: 10px;
      }}
      textarea {{
        margin: 10px 0;
        width: 540px;
        height: 120px;
      }}
    </style>
  </head>
  <body>
    <form method="POST" id="encryption">
      <p>Rotate by:</p>
      <input type="text" id="rot" name="rot" />
      <p>Input text:</p>
      <textarea name="text" id="text">{0}</textarea>
      <input type="submit" />
    </form>
  </body>
</html>

"""


@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    params = request.form.keys()
    new_message = caesar.encrypt(
        request.form["text"], int(request.form["rot"]))

    return form.format(new_message)


app.run()
