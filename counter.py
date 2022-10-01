from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ="Counter_1"

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    
    return render_template("counter.html")

@app.route("/counter")
def view_count():
        session["count"] += 1
        return redirect("/")

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)