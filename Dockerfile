FROM python:3.13-slim

WORKDIR /app

COPY app.py .

RUN python -m py_compile app.py

CMD ["python", "app.py"]