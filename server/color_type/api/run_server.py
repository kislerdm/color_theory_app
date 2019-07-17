import os
import json
from aiohttp import web
import aiohttp_cors
from typing import Tuple, Any
import pandas as pd
from color_theory_app_backend.utils import get_logger, get_args_parser
from color_theory_app_backend.api import EndPoints

# dir settings
PATH = os.path.dirname(os.path.abspath(__file__))
PATH_log = os.path.join(PATH, 'logs')

logs = get_logger(PATH_log)


class GetType(EndPoints):
    """
    Class for the end points to get the color name
    """

    payload_key = 'is_warm'
    logger = logs

    def __init__(self,
                 model: Any,
                 secrets: dict = {}):
        """
            Args:
                model: model class with the method predic
                secrets: dict with accepted APIKEYS
        """

        self.secrets = secrets
        self.model = model

    def predictor(self, r: int, g: int, b: int) -> Tuple[int, str]:
        """
        Function to predict color type based on it's RGB code

            Args:
                r: int
                g: int
                b: int

            Returns:
                tuple(color type, is_warm: int/bool, error: str)
        """
        try:
            data_point = pd.DataFrame({'r': [r], 'g': [g], 'b': [b]})

            prediction = self.model.predict(data_point)
            prediction = int(prediction)

            return prediction, None

        except Exception as err:
            self.logger.error(f"get_color_type error: {err}")
            return None, err


if __name__ == "__main__":

    # parse args
    parser = get_args_parser()

    parser.add_argument('-m', '--model_path',
                        help="Path to the model",
                        required=False, type=str,
                        default=None)

    arguments = parser.parse_args()

    # get the model
    PATH_model = arguments.model_path
    if PATH_model:
        if not os.path.isfile(PATH_model):
            logs.error(f"No model found in {PATH_model}")
            raise FileNotFoundError(f"No model found in {PATH_model}")

        from predictor.model import get_model

        model, err = get_model(PATH_model)
        if err:
            logs.error(err)
            raise Exception(err)
    else:
        logs.info("Use baseline model")
        from predictor.model import model_baseline as model

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

    endpoint = GetType(model=model, secrets=secrets)

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
        'http://localhost:10000': cors_default_opts,
        'https://color-theory-app.dkisler.com': cors_default_opts
    })

    for route in list(app.router.routes()):
        cors.add(route)

    web.run_app(app, port=port, reuse_port=True)
