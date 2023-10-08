from flask import Flask , redirect, url_for, render_template

app = Flask(__name__)

hr = False

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<num>")
def table(num):
    try:
        if hr == True:
            if int(num):
                return render_template("tables.html",num = num)
        elif hr == False:
            if int(num):
                return render_template("table.html",num = num)
    except:
        return redirect(url_for("error"))

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run()