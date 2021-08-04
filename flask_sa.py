# Vincenzo Russotto 

# local library
from s_analisys import Russentiment

# 3rd party library 
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    text = "Va che bello sto libro"
    return render_template("home.html", text=text)

@app.route("/result")
def result():
    return render_template("result.html", title="Result")

if __name__ == "__main__":
    app.run(debug=True)