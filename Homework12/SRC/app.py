# POST: додати нового студента
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    # перевірка наявності полів
    if not data or "name" not in data or "rank" not in data:
        return jsonify({"error": "Missing fields"}), 400

    # знайти останній ID
    with open(FILE, newline="") as f:
        reader = csv.DictReader(f)
        students = list(reader)
        new_id = str(len(students) + 1)

    # додати нового студента
    with open(FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "rank"])
        writer.writerow({"id": new_id, "name": data["name"], "rank": data["rank"]})

    return jsonify({"message": "Student added", "id": new_id}), 201
