import requests

BASE_URL = "http://127.0.0.1:5000/students"

def log_result(action, response):
    line = f"{action} -> {response.status_code}: {response.text}\n"
    print(line.strip())
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(line)

# 1. GET: всі студенти
resp = requests.get(BASE_URL)
log_result("GET all students (start)", resp)

# 2. POST: створити трьох студентів
students = [
    {"name": "Ivan", "rank": "A"},
    {"name": "Petro", "rank": "B"},
    {"name": "Oksana", "rank": "C"}
]
for s in students:
    resp = requests.post(BASE_URL, json=s)
    log_result(f"POST add {s['name']}", resp)

# 3. GET: всі студенти
resp = requests.get(BASE_URL)
log_result("GET all students (after POST)", resp)

# 4. PATCH: оновити rank другого студента
resp = requests.patch(f"{BASE_URL}/2", json={"rank": "D"})
log_result("PATCH update rank of student 2", resp)

# 5. GET: всі студенти (щоб перевірити другого)
resp = requests.get(BASE_URL)
log_result("GET all students (check student 2)", resp)

# 6. PUT: оновити ім’я та rank третього студента
resp = requests.put(f"{BASE_URL}/3", json={"name": "Oksana Updated", "rank": "E"})
log_result("PUT update student 3", resp)

# 7. GET: всі студенти (щоб перевірити третього)
resp = requests.get(BASE_URL)
log_result("GET all students (check student 3)", resp)

# 8. GET: всі студенти
resp = requests.get(BASE_URL)
log_result("GET all students (before DELETE)", resp)

# 9. DELETE: видалити першого студента
resp = requests.delete(f"{BASE_URL}/1")
log_result("DELETE student 1", resp)

# 10. GET: всі студенти
resp = requests.get(BASE_URL)
log_result("GET all students (final)", resp)
