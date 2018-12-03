FROM python:3.5.1
COPY /. /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000/tcp
