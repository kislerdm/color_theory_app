FROM node:12.2.0-alpine as build

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

WORKDIR /app

COPY ./app/package.json .
RUN yarn

ARG URL_BACKEND_NAME
ENV URL_BACKEND_NAME ${URL_BACKEND_NAME}

ARG URL_BACKEND_TYPE
ENV URL_BACKEND_TYPE ${URL_BACKEND_TYPE}

COPY ./app .

RUN echo 'REACT_APP_URL_BACKEND_NAME=${URL_BACKEND_NAME}' > .env \
    && echo 'REACT_APP_URL_BACKEND_TYPE=${URL_BACKEND_TYPE}' >> .env \
    && yarn build

FROM fnichol/uhttpd as serve

WORKDIR /www

COPY --from=build /app/build .
