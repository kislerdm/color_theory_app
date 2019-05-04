#!/bin/bash

# script to build the images and run micro-service containers:
# backend
# frontend

# images name
IMAGE=color_theory_app

# host ports
PORT_BE0=4500
PORT_BE=${PORT_BE0}

PORT_FE0=3000
PORT_FE=${PORT_FE0}

# backend API end-point
BACKEND_API0=http://localhost:${PORT_BE}
BACKEND_API=${BACKEND_API0}

# launch backend API
usage () {
    cat <<HELP_USAGE

    $0  -b [--port_be] -f [--port_fe] -u [--url]

   -b [--port_be] Port to expose backend API end-point [default 4500].

   -f [--port_fe] Port to serve frontend app [default 3000].

   -u [--url] URL to access backend API by the frontend app [delafut http://localhost:${PORT_BE}]

HELP_USAGE
}

msg () {
  echo "$(date +"%Y-%m-%d %H:%M:%S") $1"
}

# parse arguments
while [ "$1" != "" ]; do
    case $1 in
        -b | --port_be )        shift
                                PORT_BE=$1
                                ;;
        -f | --port_fe )        shift
                                PORT_FE=$1
                                ;;
        -u | --url )            shift
                                BACKEND_API=$1
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

# check the API URL
if [[ ( ! ${PORT_BE} -eq ${PORT_BE0} ) &&
     ( "${BACKEND_API}" == "${BACKEND_API0}" ) ]]; then
       BACKEND_API=http://localhost:${PORT_BE}
fi

# export variables
export PORT_BE=${PORT_BE}
export PORT_FE=${PORT_FE}
export BACKEND_API=${BACKEND_API}

# build and run microservices containers

docker_compose_build () {
  docker-compose -p ${IMAGE} up -d
}

msg "Build and run images for ${IMAGE}"

docker_compose_build

flag=$?
if [ ${flag} -eq 0 ]; then
  msg "Done! Access the app/frontend through the port ${PORT_FE}"
fi
