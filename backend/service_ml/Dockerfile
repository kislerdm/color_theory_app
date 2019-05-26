FROM python:3.6-slim

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

RUN mkdir -p backend/api backend/ml/model

# copy libs
WORKDIR /backend
COPY libs ./libs
RUN python3 ./libs/setup.py install

# copy model
WORKDIR /backend/ml/model
COPY service_ml/ml/model/model_v1.xgb ./model_v1.xgb

# copy service
WORKDIR /backend/api
COPY service_ml/api/run_server.py service_ml/api/requirements.txt ./
COPY service_ml/api/ml_model ./ml_model

# xgboost requirement
RUN apt-get update && apt-get install libgomp1

# py requirements install
RUN pip3 install -r requirements.txt

# get port variable
ENV PORT 4500

CMD python3 run_server.py -p ${PORT}
