FROM python:3.11-slim

WORKDIR /app

COPY /backend/requirements.txt  .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8282

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8282","--timeout", "120", "main:app"]