FROM python:3.10

ENV PYTHONUNBUFFERED=1 
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

ADD adapters /code/adapters/
ADD ports /code/ports/
ADD servers/logging /code/servers/logging/

RUN pip install --no-cache-dir -r /code/servers/logging/requirements.txt

ENTRYPOINT ["python3", "/code/servers/logging/main.py"]
