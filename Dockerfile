FROM python:3.9

COPY src/ ./src

ADD requirements.txt /

RUN userprofile=/
RUN mkdir /.dbt
ADD /profiles.yml /.dbt/

RUN pip install -r requirements.txt

CMD ["python", "./testsrc/main/python/outcomesDataProc.py"]
