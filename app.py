from flask import Flask, render_template, request
import math

app = Flask(__name__)

def euler_method(f, x0, y0, h, n):

    steps = []

    x = x0
    y = y0

    for i in range(n):

        slope = eval(
            f,
            {"__builtins__": None},
            {
                "x": x,
                "y": y,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "exp": math.exp,
                "log": math.log,
                "sqrt": math.sqrt
            }
        )

        y_next = y + h * slope
        x_next = x + h

        steps.append({
            "step": i + 1,
            "x": round(x, 6),
            "y": round(y, 6),
            "slope": round(slope, 6),
            "y_next": round(y_next, 6)
        })

        x = x_next
        y = y_next

    return steps


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        function = request.form["function"]
        x0 = float(request.form["x0"])
        y0 = float(request.form["y0"])
        h = float(request.form["h"])
        n = int(request.form["n"])

        result = euler_method(function, x0, y0, h, n)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)