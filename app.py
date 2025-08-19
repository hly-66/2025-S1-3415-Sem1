from flask import Flask,render_template,request

app = Flask(__name__)   #confirm the name of the registered person who is running the application

#gunicorn.py is a program to run wasgi and wasgi is needed for python to communicate frontend and backend

@app.route("/",methods=["GET","POST"]) #using flask framework, this is the way we are coding; "/" is the landing page for flask; methods is what you need to run before you can run anything else
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    #database
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = float(request.form.get("q"))
    return(render_template("dbs.html", r= (-50.6*q)+90.2))

if __name__ == "__main__":
    app.run()   #confirming the registered person wants to run the program