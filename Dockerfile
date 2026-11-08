FROM python:3.13-slim

WORKDIR /app

COPY app.py .

ENV PYTHONUNBUFFERED=1

USER 10001:10001

EXPOSE 8000

CMD ["python", "app.py"]
