FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]