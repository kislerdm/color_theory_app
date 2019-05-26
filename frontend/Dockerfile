# 1. build the frontend
FROM node:8.16-alpine as eng

LABEL maintainer=dkisler \
      email=admin@dkisler.de

RUN mkdir -p /app /app/src /app/public

WORKDIR /app

# backend URL
ARG APIURL_BASE
ARG APIURL_ML

COPY ./app/package.json ./app/yarn.lock ./
COPY ./app/src ./src
COPY ./app/public ./public

# use provided end-point URL
RUN sed "s;api_url;${APIURL};g" src/call.js -i

RUN yarn && yarn build

# # 2. run the app
FROM nginx:1.15.12-alpine

COPY --from=eng /app/build /usr/share/nginx/html

ENV PORT 80

EXPOSE ${PORT}

CMD ["nginx", "-g", "daemon off;"]
