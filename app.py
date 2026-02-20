from flask import Flask, render_template, request, send_file
from parser import parse_script
import io

print("APP STARTING...")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['script']
    output = parse_script(user_input)
    return render_template("index.html", output=output)

@app.route('/download', methods=['POST'])
def download():
    output=request.form['output']

    return send_file(
        io.BytesIO(output.encode()),
        as_attachment=True,
        download_name="DuckyScript.txt",
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(debug=True)