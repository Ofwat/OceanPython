FROM python:3.9

COPY src/ ./src

ADD requirements.txt /

RUN userprofile=/
RUN mkdir /.dbt
ADD /profiles.yml /.dbt/

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev 

RUN pip install -r requirements.txt

CMD ["python", "./src/main/python/outcomesDataProc.py"]
