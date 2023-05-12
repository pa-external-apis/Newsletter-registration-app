 
FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app

ENV SQL_USERNAME=newsletter_UN
ENV SQL_PASSWORD=TsP2idtRSvAPMSWcTD9i
ENV SQL_SERVER=newslettersqlserver
ENV SQL_DB=news
ENV TABLE_NAME=news_subscribers

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
