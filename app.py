from flask import Flask, render_template_string, request, send_from_directory
import os

app = Flask(__name__)

# HTML template with a text field and a checkbox
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

# Route for the main page
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form.get("textfield")
        check = request.form.get("check")
        result = f"Text: {text}, Checkbox: {check}"
    return render_template_string(html, result=result)

# Route to serve the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

