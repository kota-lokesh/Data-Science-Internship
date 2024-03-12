from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("home.html")
    return render_template("home.html")

@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        matches = re.findall(regex_pattern, test_string)
        return render_template("results_regex.html", matches=matches)

@app.route("/email",methods=["POST"])
def email_valid():
    validation_result = None
    if request.method=="POST":
        test_mail = request.form.get("test_email")
        pattern = "\w+@\w+.\w+"
        matches = re.match(pattern,test_mail)
        if re.match(pattern, test_mail):
            validation_result = "Valid Email"
        else:
            validation_result = "Invalid Email"
    return render_template("home.html",validation_result=validation_result)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

