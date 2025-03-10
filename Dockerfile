FROM python:3.9.1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python3 bot.py
CMD python3 annabelle.py
