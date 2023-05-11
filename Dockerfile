FROM tiangolo/uvicorn-gunicorn:python3.10


COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app

ENTRYPOINT uvicorn --host 0.0.0.0 main:app 