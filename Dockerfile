FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 9090
EXPOSE 443

CMD ["python", "app.py"]
