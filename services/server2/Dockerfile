FROM python:3.10

ENV PYTHONBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

COPY adapters /code/adapters/
COPY ports /code/ports/
COPY services/server2 /code/services/server2/

RUN pip install --no-cache-dir -r /code/services/server2/requirements.txt

ENTRYPOINT ["python3", "/code/services/server2/main.py"]
