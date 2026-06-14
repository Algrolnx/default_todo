FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY todoList/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/todoList

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]