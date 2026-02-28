from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from parser import parse_script
import io

print("APP STARTING...")

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.json.get("script")
    output = parse_script(user_input)
    return jsonify({"output": output})

@app.route("/download", methods=["POST"])
def download():
    output = request.json.get("output")

    return send_file(
        io.BytesIO(output.encode()),
        as_attachment=True,
        download_name="DuckyScript.txt",
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(debug=True)