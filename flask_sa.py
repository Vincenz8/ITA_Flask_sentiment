# Vincenzo Russotto 

# local libraries
from s_analisys import Russentiment as rs 

# 3rd party libraries 
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
    
    analisys = rs.result(p_text) #analisys
    
    return render_template("result.html", title="Result", analisys=analisys)

if __name__ == "__main__":
    app.run()