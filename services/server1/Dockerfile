FROM python:3.10

ENV PYTHONBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

ADD adapters /code/adapters/
ADD services/server1 /code/services/server1/

RUN pip install --no-cache-dir -r /code/services/server1/requirements.txt

ENTRYPOINT ["python3", "/code/services/server1/main.py"]
