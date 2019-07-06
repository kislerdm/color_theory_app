FROM python:3.7-slim as base

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

FROM base as builder

RUN mkdir -p /app/api /app/data

# copy libs
WORKDIR /app
COPY common_libs ./libs
COPY color_name/api/requirements.txt ./

# py requirements install
RUN pip install --no-cache-dir -r ./requirements.txt

# copy service
COPY color_name/api ./api
COPY color_name/data ./data

# get port variable
ENV PORT 4500

CMD python3 ./api/run_server.py -p ${PORT}
