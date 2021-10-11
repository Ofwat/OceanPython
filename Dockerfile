FROM python:3.9

RUN mkdir /testsrc
COPY src/ /testsrc

ADD requirements.txt /

RUN userprofile=/
RUN mkdir /.dbt
ADD /profiles.yml /.dbt/

RUN pip install -r requirements.txt

CMD ["python", "./testsrc/main/python/outcomesDataProc.py"]
