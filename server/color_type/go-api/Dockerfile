FROM golang:1.11-alpine AS build

WORKDIR /app

COPY ./ColorType .

RUN go build -o run_server *.go \
    && rm *.go

CMD ./run_server