FROM svizor/zoomcamp-model:3.9.12-slim

RUN [ "pip", "install", "pipenv" ]

WORKDIR /app

COPY ["Pipfile.lock", "Pipfile", "."]

RUN [ "pipenv", "install", "--deploy", "--system"]

COPY ["*.py", "dv.bin", "model1.bin", "."]

EXPOSE 8080

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080", "solution_question4:app" ]
