FROM python:3.6-slim

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

RUN mkdir -p backend/api

# copy libs
WORKDIR /backend
COPY libs ./libs
COPY service_base/api/requirements.txt ./api/

# py requirements install
RUN pip3 install -r ./api/requirements.txt
RUN python3 ./libs/setup.py install

# copy service
WORKDIR /backend/api
COPY service_base/api ./

# get port variable
ENV PORT 4500

CMD python3 run_server.py -p ${PORT}
