FROM python:3.11-slim


WORKDIR /app
COPY  ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . /app



# RUN pip install requests

CMD ["python3", "req.py"]

# Закомментированные команды для сборки и запуска образ
# docker build -t request_service:1 .
