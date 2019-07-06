import os
import json
from aiohttp import web
import aiohttp_cors
import pandas as pd
import numpy as np
from typing import Tuple
from color_theory_app_backend.utils import get_logger, get_args_parser
from color_theory_app_backend.api import EndPoints


# dir settings
PATH = os.path.dirname(os.path.abspath(__file__))
PATH_log = os.path.join(PATH, 'logs')

logs = get_logger(PATH_log)

# dir for data set
PATH_data = os.path.join(os.path.dirname(PATH), 'data/colors.csv')

if not os.path.isfile(PATH_data):
    logs.error(f"No data found in {PATH_data}")
    raise FileNotFoundError(f"No data found in {PATH_data}")

try:
    dat = pd.read_csv(PATH_data)

except Exception as err:
    logs.error(f"Cannot read the model from {PATH_data}\nError: {err}")
    raise Exception(err)


class GetName(EndPoints):
    """
    Class for the end points to get the color name
    """

    payload_key = 'name'
    logger = logs

    def __init__(self,
                 data: pd.DataFrame,
                 secrets: dict = {}):
        """
            Args:
                data: pd.DataFrame data sample
                secrets: dict with accepted APIKEYS
        """

        self.secrets = secrets
        self.r = data['r'].astype(np.int16)
        self.g = data['g'].astype(np.int16)
        self.b = data['b'].astype(np.int16)
        self.color_name = data['color_name']

    def predictor(self, r: int, g: int, b: int) -> Tuple[str, str]:
        """
        Function to predict color name based on it's RGB code

            Args:
                r: int
                g: int
                b: int

            Returns:
                tuple(color name: str, error: str)
        """

        def _square(x0, x):
            return np.square(x0 - x)

        try:

            color_dist = np.sqrt(_square(self.r, float(r))
                                 + _square(self.g, float(g))
                                 + _square(self.b, float(b)))

            color = self.color_name[np.where(color_dist == color_dist.min())[0][0]]

            return color, None

        except Exception as err:
            self.logger.error(f"get_color_name error: {err}")
            return '', err


if __name__ == '__main__':

    # parse args
    parser = get_args_parser()
    arguments = parser.parse_args()

    port = arguments.port

    PATH_secrets = arguments.secrets
    secrets = {}
    if PATH_secrets:
        if os.path.isfile(PATH_secrets):
            try:
                secrets = json.load(open(PATH_secrets, 'r'))

            except Exception as err:
                logs.error(f"Cannot read secrets\nError: {err}")
                pass

    logs.info(f"Launch API through port {port}")

    endpoint = GetName(data=dat, secrets=secrets)

    app = web.Application()

    app.router.add_get("/rgb", endpoint.on_rgb)
    app.router.add_get("/hex", endpoint.on_hex)

    # make CORS
    cors_default_opts = aiohttp_cors.ResourceOptions(allow_credentials=False,
                                                     expose_headers="*",
                                                     allow_headers=("Content-Type", "APIKEY"),
                                                     allow_methods=["GET"])

    cors = aiohttp_cors.setup(app, defaults={
        'http://localhost:3000': cors_default_opts,
        'http://localhost:10000': cors_default_opts
    })

    for route in list(app.router.routes()):
        cors.add(route)

    web.run_app(app, port=port, reuse_port=True)
