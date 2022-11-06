FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["model.bin", "predict.py", "predict_test.py", "./"] 

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]
