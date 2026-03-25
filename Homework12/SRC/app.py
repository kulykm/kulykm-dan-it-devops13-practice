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

# POST: додати нового студента
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data or "name" not in data or "rank" not in data:
        return jsonify({"error": "Missing fields"}), 400

    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        students = list(reader)
        new_id = str(len(students) + 1)

    with open(FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "rank"])
        writer.writerow({"id": new_id, "name": data["name"], "rank": data["rank"]})

    return jsonify({"message": "Student added", "id": new_id}), 201

# PUT: оновити всі дані студента за ID
@app.route("/students/<id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    if not data or "name" not in data or "rank" not in data:
        return jsonify({"error": "Missing fields"}), 400

    updated = False
    students = []

    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == id:
                row["name"] = data["name"]
                row["rank"] = data["rank"]
                updated = True
            students.append(row)

    if not updated:
        return jsonify({"error": "Student not found"}), 404

    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "rank"])
        writer.writeheader()
        writer.writerows(students)

    return jsonify({"message": "Student updated", "id": id}), 200

# PATCH: оновити окремі поля студента за ID
@app.route("/students/<id>", methods=["PATCH"])
def patch_student(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    updated = False
    students = []

    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == id:
                if "name" in data:
                    row["name"] = data["name"]
                if "rank" in data:
                    row["rank"] = data["rank"]
                updated = True
            students.append(row)

    if not updated:
        return jsonify({"error": "Student not found"}), 404

    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "rank"])
        writer.writeheader()
        writer.writerows(students)

    return jsonify({"message": "Student partially updated", "id": id}), 200

# DELETE: видалити студента за ID
@app.route("/students/<id>", methods=["DELETE"])
def delete_student(id):
    deleted = False
    students = []

    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == id:
                deleted = True
                continue
            students.append(row)

    if not deleted:
        return jsonify({"error": "Student not found"}), 404

    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "rank"])
        writer.writeheader()
        writer.writerows(students)

    return jsonify({"message": "Student deleted", "id": id}), 200

if __name__ == "__main__":
    app.run(debug=True)
