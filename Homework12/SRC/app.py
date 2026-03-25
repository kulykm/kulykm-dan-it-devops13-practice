from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
FILE = "students.csv"

# Ініціалізація CSV, якщо його немає
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "rank"])
        writer.writeheader()

# GET: всі студенти
@app.route("/students", methods=["GET"])
def get_students():
    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        return jsonify(list(reader))

if __name__ == "__main__":
    app.run(debug=True)
