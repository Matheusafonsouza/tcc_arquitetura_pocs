FROM python:3.10

ENV PYTHONBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

COPY adapters /code/adapters/
COPY ports /code/ports/
COPY services/server3 /code/services/server3/

RUN pip install --no-cache-dir -r /code/services/server3/requirements.txt

ENTRYPOINT ["python3", "/code/services/server3/main.py"]
