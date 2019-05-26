FROM python:3.6-slim

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

RUN mkdir -p backend/api

# copy libs
WORKDIR /backend
COPY libs ./libs
RUN python3 ./libs/setup.py install

# copy service
WORKDIR /backend/api
COPY service_base/api/run_server.py service_base/api/requirements.txt ./
COPY service_base/api/color_name ./color_name

# py requirements install
RUN pip3 install -r requirements.txt

# get port variable
ENV PORT 4499

CMD python3 run_server.py -p ${PORT}
