FROM python:3.9.19-slim-bullseye

WORKDIR /app

COPY main.py /app/

CMD ["python", "main.py"]
