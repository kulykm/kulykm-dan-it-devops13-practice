# Базовий образ Python, щоб працював Flask
FROM python:3.10-slim

# Всередині контейнера буде папка /app
WORKDIR /app

# Копіюємо код з домашки №12 (app.py і requirements.txt)
COPY . /app

# Встановлюємо бібліотеки з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо наш Flask API через gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
