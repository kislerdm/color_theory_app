FROM python:3.6-slim

LABEL maintainer=dkisler \
      email=admin@dkisler.de

RUN mkdir -p backend/api backend/ml/model

# copy model
WORKDIR /backend/ml/model
COPY ml/model/model_v1.xgb ./model_v1.xgb

# copy service
WORKDIR /backend/api
COPY api/run_server.py api/requirements.txt ./
COPY api/ml_model ./ml_model

# xgboost requirement
RUN apt-get update && apt-get install libgomp1

RUN pip3 install -r requirements.txt

CMD python3 run_server.py
