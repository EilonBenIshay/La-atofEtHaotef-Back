FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
ADD backend backend

EXPOSE 9090
EXPOSE 443

CMD ["python", "backend/contgrollers/posts_controller.py"]
