FROM python:3.9

ADD src/main/python/outcomesDataProc.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "src/main/python/outcomesDataProc.py"]
