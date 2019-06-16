FROM node:12.2.0-alpine

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

RUN mkdir -p /app/src /app/public

WORKDIR /app

COPY ./app/package.json ./
COPY ./app/.env ./
COPY ./app/src ./src
COPY ./app/public ./public

RUN yarn install
RUN yarn build
RUN yarn global add serve

ENV PORT 80

CMD serve -s build -p ${PORT}
