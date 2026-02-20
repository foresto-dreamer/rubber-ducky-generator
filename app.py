from flask import Flask, render_template, request
from parser import parse_script

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

if __name__ == "__main__":
    app.run(debug=True)