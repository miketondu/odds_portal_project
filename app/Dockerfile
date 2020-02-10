FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./model.pkl /deploy/
COPY ./model_columns.pkl /deploy/
COPY ./templates /deploy/templates/
COPY ./static /deploy/static/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]
