FROM python:3

WORKDIR /app
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD bash /app/run.sh