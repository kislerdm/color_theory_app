FROM python:3.7-slim as base

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

FROM base as builder

RUN mkdir -p /install /serve/api /model

# copy libs
WORKDIR /install
COPY common_libs ./libs
COPY color_type/api/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

# copy service
WORKDIR /serve
COPY color_type/api ./

# install xgboost
RUN apt-get update \
    && apt-get install -y libgomp1 \
    && pip --no-cache-dir install xgboost scikit-learn \
    && apt-get autoremove -y

# path to model
WORKDIR /model
ENV PATH_model="/model"
ENV MODEL model_v2.sav
COPY color_type/ml/model/v2/${MODEL} ./${MODEL}

# get port variable
ENV PORT 4500

CMD python3 /serve/run_server.py -p ${PORT} -m ${PATH_model}/${MODEL}
