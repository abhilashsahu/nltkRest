FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /app_source

WORKDIR /app_source

COPY requirements.txt /app_source

RUN pip3.10 install -r requirements.txt

RUN python3.10 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt');"

COPY . .

EXPOSE 8000