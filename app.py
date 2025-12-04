from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")     # <<< Không dùng "Hello Client" nữa

@app.route("/api/students")
def get_students_from_csv():
    try:
        df = pd.read_csv("students_dropout_academic_success.csv")
        data = df.to_dict(orient="records")
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)

