FROM python:3.10-alpine
WORKDIR /web_app
ENV FLASK_APP=app
COPY .requirements/requirements-app.txt .
RUN pip install --upgrade pip && pip install -r requirements-app.txt && apk update && apk add python3-dev gcc libc-dev
COPY app/ app/
ENV FLASK_APP=app
CMD ["flask", "run", "--port=5000", "--host=0.0.0.0"]


# docker-compose exec web flask db init
# docker-compose exec web flask db migrate
# docker-compose exec web flask db upgrade
