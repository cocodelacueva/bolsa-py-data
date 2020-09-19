FROM python:3.8.5
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt