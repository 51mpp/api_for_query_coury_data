FROM python:3.9-slim
WORKDIR /api_for_query_coutry_data:
COPY app.py /api_for_query_coutry_data/
COPY requirements.txt /api_for_query_coutry_data/
RUN pip install --upgrade pip setuptools wheel --user
RUN pip install -r requirements.txt
ENV TZ="Asia/Bangkok"
CMD ["python","app.py"]
EXPOSE 34567