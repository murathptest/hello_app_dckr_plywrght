from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
<h1>Hello World App</h1>
<form method="POST">
    <label>Enter Text:</label>
    <input type="text" name="textfield">
    <br>
    <label>Check me:</label>
    <input type="checkbox" name="check" value="yes">
    <br><br>
    <input type="submit" value="Submit">
</form>
{% if result %}
<h2>You submitted:</h2>
<p>{{ result }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form.get("textfield")
        check = request.form.get("check")
        result = f"Text: {text}, Checkbox: {check}"
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
