FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./model.pkl /deploy/
COPY ./model_columns.pkl /deploy
COPY ./templates/index.html /deploy
COPY ./static/css/style.css /deploy
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
