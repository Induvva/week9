from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    show_form = True
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        if name and email:
            show_form = False
            message = f"Thanks {name}! You have successfully registered for the event using {email}."
        else:
            message = "Please fill in both name and email."
    return render_template("index.html", show_form=show_form, message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)