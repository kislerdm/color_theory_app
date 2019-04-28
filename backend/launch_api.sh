#!/bin/bash

# dafaults
PORT=4500
IMAGE=backend_color_app_api:latest
FORCE=0
RERUN=0

DIRLOG="$( cd "$(dirname "$0")" ; pwd -P )"/logs

if [ ! -f ${DIRLOG} ]; then
  mkdir -p ${DIRLOG}
fi

# launch backend API
usage () {
    cat <<HELP_USAGE

    $0  -p [--port] -f [--force]

   -p [--port]  Port to expose [default 4500].

   -f [--force] Force re-build image [delafut 0]

   -r [--rerun] Force re-start container [delafut 0]

HELP_USAGE
}

msg () {
  echo "$(date +"%Y-%m-%d %H:%M:%S") $1"
}

# parse arguments
while [ "$1" != "" ]; do
    case $1 in
        -p | --port )           shift
                                PORT=$1
                                ;;
        -f | --force )          shift
                                FORCE=1
                                ;;
        -r | --rerun )          shift
                                RERUN=1
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

docker_run () {
  docker run -d -v ${DIRLOG} -e PORT=${PORT} -p ${PORT}:${PORT} -t ${IMAGE}
}

# check if image was built
imageId=$(docker images ${IMAGE} -q)

if [[ ("${imageId}" == "") || (${FORCE} -eq 1) ]]; then
  msg "Build image ${IMAGE}"

  docker build -t ${IMAGE} .
fi

# run API service container
runner=1
while [ ${runner} -eq 1 ]; do
  msg "Run container of the image ${IMAGE} through port ${PORT}"
  docker_run
  flag=$?

  if [ ${flag} -eq 0 ]; then
    runner=0
  else
    msg "Port ${PORT} is busy"

    if [ ${RERUN} -eq 1 ]; then
      msg "Re-run activated -> stop the container"
      docker stop $(docker ps | grep "\:${PORT}->" | cut -d' ' -f1)
    else
      msg "Re-run container through different port? [yn]"

      read inpt

      if [[ ("${inpt}" == "y") || ("${inpt}" == "Y") ]]; then
        msg "Enter the port"
        read PORT
      else
        msg "Re-run container? [yn]"
        read inpt
        if [[ ("${inpt}" == "y") || ("${inpt}" == "Y") ]]; then
          RERUN=1
        else
          exit 1
        fi
      fi

    fi
  fi

done

msg "API has launched successfully"
