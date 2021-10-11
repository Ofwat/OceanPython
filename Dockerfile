FROM python:3.9

COPY src/ ./src

ADD requirements.txt /

RUN userprofile=/
RUN mkdir /.dbt
ADD /profiles.yml /.dbt/

ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

RUN pip install -r requirements.txt

CMD ["python", "./src/main/python/outcomesDataProc.py"]
