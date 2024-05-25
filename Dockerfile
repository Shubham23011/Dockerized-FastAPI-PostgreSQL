FROM python:3.12.3

WORKDIR /code

COPY requirements.txt ./

COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/code

RUN pip install psycopg2-binary

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80" ]