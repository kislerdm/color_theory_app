FROM python:3.6-slim

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

RUN mkdir -p backend/api backend/ml/model

# copy libs
WORKDIR /backend
COPY libs ./libs
COPY service_ml/api/requirements.txt ./api/requirements.txt

# py install requirementes
RUN python3 ./libs/setup.py install
# xgboost requirements
RUN apt-get update && apt-get install libgomp1
RUN pip3 install -r ./api/requirements.txt

# copy service
WORKDIR /backend/api
COPY service_ml/api ./

# copy model
WORKDIR /backend/ml/model
COPY service_ml/ml/model/model_v1.xgb ./model_v1.xgb

# get port variable
ENV PORT 4500

CMD python3 /backend/api/run_server.py -p ${PORT}
