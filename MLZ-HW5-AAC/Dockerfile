FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock",  "./"]

RUN pipenv install  --deploy --system

COPY ["predict_docker.py", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress", "--bind=0.0.0.0:9696", "suscription:app"]

