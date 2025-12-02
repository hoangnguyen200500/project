from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)  # Kích hoạt CORS cho toàn bộ ứng dụng, cho phép mọi domain đều có thể truy cập

@app.route('/')
def home():
    return "Hello, Client!"

@app.route('/api/students')
def get_students_from_csv():
    try:
        df = pd.read_csv("./students_dropout_academic_success.csv")  # đảm bảo đúng đường dẫn
        data = df.to_dict(orient="records")
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
