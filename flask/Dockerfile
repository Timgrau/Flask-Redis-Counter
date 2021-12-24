FROM python:3.8-bullseye

WORKDIR /usr/app/src
COPY app.py templates ./
RUN mkdir templates && mv hello.html templates/ && \
    pip install --no-cache-dir redis flask flask-wtf && ls
EXPOSE 6379

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
