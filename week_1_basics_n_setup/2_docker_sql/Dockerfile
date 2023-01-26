# FROM python


# RUN pip install pandas

# WORKDIR /app
# COPY pipeline.py pipeline.py

# # ENTRYPOINT [ "bash" ]
# ENTRYPOINT [ "python", "pipeline.py" ]

FROM python

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT [ "python", "ingest_data.py" ]