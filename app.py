from flask import Flask, render_template, request
from analyzer import analyze_code
from metrics import complexity_score
from suggestions import give_suggestions

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form["code"]

    analysis = analyze_code(code)
    complexity = complexity_score(code)
    tips = give_suggestions(complexity)

    return render_template(
        "result.html",
        analysis=analysis,
        complexity=complexity,
        tips=tips
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
