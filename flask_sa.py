# Vincenzo Russotto 

# local library
from s_analisys import Russentiment as rs 

# 3rd party library 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result", methods = ["post"])
def result():
    
    text = request.form.get("text", type= str)
    t_text = rs.cleaned_text(text) #tokenized text
    p_text = rs.polarity_text(t_text) #polarity of the text
    pred = rs.pred(p_text) #prediction
    
    return render_template("result.html", title="Result", pred=pred)

if __name__ == "__main__":
    app.run()