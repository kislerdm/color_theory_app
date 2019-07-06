FROM node:12.2.0-alpine as build

LABEL maintainer="Dmitry Kisler" \
      email=admin@dkisler.com \
      web=www.dkisler.com

WORKDIR /app

COPY ./app/package.json .
RUN yarn

COPY ./app .

RUN yarn build

FROM fnichol/uhttpd as serve

WORKDIR /www

COPY --from=build /app/build .
