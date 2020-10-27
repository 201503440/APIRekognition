FROM python
RUN pip install Flask
RUN pip install boto3
RUN pip install --upgrade localstack-client
RUN pip install -U flask-cors
COPY . .
CMD [ "python3", "./main.py" ]