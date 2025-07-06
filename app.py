from flask import flask
app = flask(__name__)

@app.route("/info")
def lwinfo():
        return "i m LW from India"

@app.route("/phone")
 def lwphone():
         return"93516666689"

app.run(host="0.0.0.0")