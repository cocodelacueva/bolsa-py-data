FROM python:3.8.5
COPY requirements.txt ./app
RUN pip install --no-cache-dir -r requirements.txt
