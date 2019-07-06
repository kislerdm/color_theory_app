#!/bin/bash

# script to build the images and run micro-service containers:
# server/backend
# client/frontend

# images name
IMAGE=color_theory_app
FILE=docker-compose.yaml

# ports
PORT_FE0=10000
PORT_FE=${PORT_FE0}

PORT_BE_NAME0=10002
PORT_BE_NAME=${PORT_BE_NAME0}

PORT_BE_TYPE0=10003
PORT_BE_TYPE=${PORT_BE_TYPE0}


# backend API end-point
BACKEND_API_NAME0="http://0.0.0.0:${PORT_BE_NAME}/hex"
BACKEND_API_NAME=${BACKEND_API_NAME0}

BACKEND_API_TYPE0="http://0.0.0.0:${PORT_BE_TYPE}/hex"
BACKEND_API_TYPE=${BACKEND_API_TYPE0}

# flags
FORCE=0

# launch backend API
usage () {
    cat <<HELP_USAGE

    ${IMAGE} launcher

    Run: sh $0 [--file --image --force --port_be_name --port_be_type --port_fe --url_name --url_type]

   --file docker-compose file [optional; detauls ${FILE}]

   --image image name [optional; 0, or 1: default ${IMAGE}]

   --force force rebuild [optional; default ${FORCE}]
   
   --port_fe Port to serve client app [optional; default ${PORT_FE0}]

   --port_be_name Port to expose backend color_name serivce API end-point [optional; default ${PORT_BE_NAME0}]

   --port_be_type Port to expose backend color_type service API end-point [optional; default ${PORT_BE_TYPE0}]

   --url_name URL to access backend BASE API by the frontend app [optional; delafut ${BACKEND_API_NAME0}]

   --url_type URL to access backend ML API by the frontend app [optional; delafut ${BACKEND_API_TYPE0}]

HELP_USAGE
}

msg () {
  echo "$(date +"%Y-%m-%d %H:%M:%S") $1"
}

# parse arguments
while [ "$1" != "" ]; do
    case $1 in
        --file )                shift
                                FILE=$1
                                ;;
        --image )               shift
                                IMAGE=$1
                                ;;
        --force )               shift
                                FORCE=1
                                ;;
        --port_fe )             shift
                                PORT_FE=$1
                                ;;                                
        --port_be_name )        shift
                                PORT_BE_NAME=$1
                                ;;
        --port_be_type )        shift
                                PORT_BE_TYPE=$1
                                ;;        
        --url_name )            shift
                                BACKEND_API_NAME=$1
                                ;;
        --url_type )            shift
                                BACKEND_API_TYPE=$1
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

if [ ! -f ${FILE} ]; then
  msg "File ${FILE} doesn't exist"
  exit 1
fi

# check the API URL
if [[ ( ! ${PORT_BE_NAME} -eq ${PORT_BE_NAME0} ) &&
     ( "${BACKEND_API_NAME}" == "${BACKEND_API_NAME0}" ) ]]; then
       BACKEND_API_NAME="http://0.0.0.0:${PORT_BE_NAME}/hex"
fi

if [[ ( ! ${PORT_BE_TYPE} -eq ${PORT_BE_TYPE0} ) &&
     ( "${BACKEND_API_TYPE}" == "${BACKEND_API_TYPE0}" ) ]]; then
       BACKEND_API_TYPE="http://0.0.0.0:${PORT_BE_TYPE}/hex"
fi

# export variables
export PORT_BE_NAME=${PORT_BE_NAME}
export PORT_BE_TYPE=${PORT_BE_TYPE}
export PORT_FE=${PORT_FE}
export BACKEND_API_NAME=${BACKEND_API_NAME}
export BACKEND_API_TYPE=${BACKEND_API_TYPE}

# build and run microservices containers

docker_compose_build () {
  if [ ${FORCE} -eq 1 ]; then
    docker-compose -p ${IMAGE} -f ${FILE} up -d --build
  else
    docker-compose -p ${IMAGE} -f ${FILE} up -d
  fi
}

msg "Build and run images for ${IMAGE}"

docker_compose_build

flag=$?
if [ ${flag} -eq 0 ]; then
  msg "Done! Access the app/frontend through the port ${PORT_FE}"
fi
