FROM python:3.10

ENV PYTHONUNBUFFERED=1 
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

COPY adapters /code/adapters/
COPY ports /code/ports/
COPY services/logging /code/services/logging/

RUN pip install --no-cache-dir -r /code/services/logging/requirements.txt

ENTRYPOINT ["python3", "/code/services/logging/main.py"]
