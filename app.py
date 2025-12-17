from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        products.append({
            "name": request.form["name"],
            "price": request.form["price"],
            "image": request.form["image"]
        })
        return redirect(url_for("index"))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
