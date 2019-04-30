import os
import sys
import time
from aiohttp import web
import aiohttp_cors
import argparse
import logging
from ml_model.endpoints import EndPoints
from ml_model.predictor import Predict


# end-pount settings
PORT = 4500
CONTENT_TYPE = 'applicaiton/json'

# dir settings
PATH = os.path.dirname(os.path.abspath(__file__))
PATH_log = os.path.join(PATH, 'logs')

# dir for model
DIR_model = os.path.join(os.path.dirname(PATH), 'ml/model')
MODEL = 'model_v1.xgb'

PATH_model = os.path.join(DIR_model, MODEL)

if not os.path.isfile(PATH_model):
    print(f'No model found in in {PATH_model}')
    sys.exit(1)


def get_args():
    """
    Parser for input arguments
    """

    parser = argparse.ArgumentParser(add_help=True,
                                     description="Backend ML API")
    parser.add_argument('-p', '--port',
                        help="Port to expose the API end-points",
                        default=PORT, type=int)

    return parser.parse_args()


def get_logger(log_path: str) -> logging.getLogger:
    """
    Initiate logger instance

            Args:
                log_path: str path to log file

            Returns:
                logger
    """

    path = os.path.dirname(log_path)
    if not os.path.isdir(path):
        os.makedirs(path)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=log_path,
                        filemode='a+')

    return logging.getLogger('logs')


if __name__ == '__main__':

    path_log = os.path.join(PATH_log, 'ml_api_{}.log'.format(
        time.strftime('%Y%m%d', time.localtime())))
    logger = get_logger(path_log)

    # parse args
    argumets = get_args()
    port = argumets.port

    logger.info(f"Launch API throuh port {port}")

    try:
        # get the model
        predictor = Predict(logger=logger, path_model=PATH_model)

        # # get endpoints
        endpoint = EndPoints(
            logger=logger, predictor=predictor, content_type=CONTENT_TYPE)

    except Exception as e:
        logger.error(e)
        print(e)
        sys.exit(1)

    app = web.Application()

    app.router.add_get("/rgb", endpoint.get_color_cat_rgb)
    app.router.add_get("/hex", endpoint.get_color_cat_hex)

    # make CORS
    cors_default_opts = aiohttp_cors.ResourceOptions(allow_credentials=True,
                                                     expose_headers="*",
                                                     allow_headers="*",
                                                     allow_methods=["GET"])

    cors = aiohttp_cors.setup(app, defaults={
        "https://www.dkisler.de": cors_default_opts,
        "http://localhost:3000": cors_default_opts,
        "http://color-theory-app.s3-website-eu-west-1.amazonaws.com/": cors_default_opts
    })

    for route in list(app.router.routes()):
        cors.add(route)

    web.run_app(app, port=port, reuse_port=True)
