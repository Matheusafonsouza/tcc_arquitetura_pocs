FROM python:3.10

ENV PYTHONBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

ADD adapters /code/adapters/
ADD ports /code/ports/
ADD servers/server1 /code/servers/server1/

RUN pip install --no-cache-dir -r /code/servers/server1/requirements.txt

ENTRYPOINT ["python3", "/code/servers/server1/main.py"]
