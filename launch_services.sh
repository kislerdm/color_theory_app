#!/bin/bash

# script to build the images and run micro-service containers:
# backend
# frontend

# images name
IMAGE=color_theory_app

# host ports
PORT_BE_ML0=4500
PORT_BE_ML=${PORT_BE_ML0}

PORT_BE_BASE0=4499
PORT_BE_BASE=${PORT_BE_BASE0}

PORT_FE0=3000
PORT_FE=${PORT_FE0}

# backend API end-point
BACKEND_API_ML0=http://localhost:${PORT_BE_ML}
BACKEND_API_ML=${BACKEND_API_ML0}

BACKEND_API_BASE0=http://localhost:${PORT_BE_BASE}
BACKEND_API_BASE=${BACKEND_API_BASE0}

# flags
FORCE=0

# launch backend API
usage () {
    cat <<HELP_USAGE

    $0 --force --port_be_base --port_be_ml --port_fe --urlbase --urlml

   --force force rebuild

   --port_be_base Port to expose backend BASE API end-point [default 4499].

   --port_be_ml Port to expose backend ML API end-point [default 4500].

   --port_fe Port to serve frontend app [default 3000].

   --urlbase URL to access backend BASE API by the frontend app [delafut ${BACKEND_API_BASE0}]

   --urlml URL to access backend ML API by the frontend app [delafut ${PORT_BE_ML0}]

HELP_USAGE
}

msg () {
  echo "$(date +"%Y-%m-%d %H:%M:%S") $1"
}

# parse arguments
while [ "$1" != "" ]; do
    case $1 in
        --force )               shift
                                FORCE=1
                                ;;
        --port_be_base )        shift
                                PORT_BE_BASE=$1
                                ;;
        --port_be_ml )          shift
                                PORT_BE_ML=$1
                                ;;
        --port_fe )             shift
                                PORT_FE=$1
                                ;;
        --urlbase )             shift
                                BACKEND_API_BASE=$1
                                ;;
        --urlml )               shift
                                BACKEND_API_ML=$1
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
if [[ ( ! ${PORT_BE_BASE} -eq ${PORT_BE_BASE0} ) &&
     ( "${BACKEND_API_BASE}" == "${BACKEND_API_BASE0}" ) ]]; then
       BACKEND_API_BASE=http://localhost:${PORT_BE_BASE}
fi

if [[ ( ! ${PORT_BE_ML} -eq ${PORT_BE_ML0} ) &&
     ( "${BACKEND_API_ML}" == "${BACKEND_API_ML0}" ) ]]; then
       BACKEND_API_ML=http://localhost:${PORT_BE_ML}
fi

# export variables
export PORT_BE_BASE=${PORT_BE_BASE}
export PORT_BE_ML=${PORT_BE_ML}
export PORT_FE=${PORT_FE}
export BACKEND_API_BASE=${BACKEND_API_BASE}
export BACKEND_API_ML=${BACKEND_API_ML}

# build and run microservices containers

docker_compose_build () {
  if [ ${FORCE} -eq 1 ]; then
    docker-compose -p ${IMAGE} up -d --build
  else
    docker-compose -p ${IMAGE} up -d
  fi
}

msg "Build and run images for ${IMAGE}"

docker_compose_build

flag=$?
if [ ${flag} -eq 0 ]; then
  msg "Done! Access the app/frontend through the port ${PORT_FE}"
fi
