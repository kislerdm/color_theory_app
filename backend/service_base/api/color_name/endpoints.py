import json
import pandas as pd
import numpy as np
from aiohttp import web
from typing import Tuple
from color_theory_app_backend_libs.utils import hex2rgb


class EndPoints:
    """
    Class for base API endpoints
    """

    def __init__(self,
                 logger,
                 data: pd.DataFrame,
                 secrets: dict = None,
                 content_type: str = 'applicaiton/json'):
        """
            Args:
                logger: logging instance
                data: pd.DataFrame data sample
                secrets: dict with accepted APIKEYS
                content_type: API response type
        """

        self.content_type = content_type
        self.logger = logger
        self.secrets = secrets
        self.r = data['r'].astype(np.int16)
        self.g = data['g'].astype(np.int16)
        self.b = data['b'].astype(np.int16)
        self.color_name = data['color_name']

    def _response_api(self, payload=None) -> web.Response:
        """
        Function to build the endpoint response

        Args:
            payload: array/dict to return on API call

        Returns:
            web.Response
        """

        if not payload:
            return web.json_response({"data": None},
                                     status=500)

        return web.json_response(payload,
                                 status=200)

    def _get_color_name(self, r: int, g: int, b: int) -> Tuple[str, str]:
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

        except Exception as e:
            self.logger.error(f"get_color_name error: {e}")
            return '', e

    def _get_payload(self, r: int, g: int, b: int) -> dict:

        prediction, err = self._get_color_name(r, g, b)

        if err:
            return None

        return {'data': {
                    "color": {'r': r, 'g': g, 'b': b},
                    'name': prediction
                    }
                }

    async def _is_auth(self, headers) -> web.Response:
        """
        Function to test client authenticaiton
            Args:
                headers: request API headers dict

            Returns:
                web.Response
        """

        if headers.get('APIKEY') is None:
            return False, "No APIKEY provided"

        if headers.get('APIKEY') not in self.secrets.values():
            return False, "Wrong APIKEY provided"

        return True, None


    async def get_color_name_hex(self, request):
        """
        Function to get the color name by it's HEX code
            Args:
                request API request with HEX parameter query string

            Returns:
                web.Response
        """

        try:
            flag, err = await self._is_auth(headers=request.headers)
            if err:
                return web.HTTPForbidden(content_type=self.content_type,
                                         text=err)

            if "hexcode" not in request.query.keys():
                return self._response_api()

            hexcode = request.query['hexcode']
            rgb, err = hex2rgb(hexcode)

            if err:
                self.logger.error(err)
                return self._response_api()

            payload = self._get_payload(rgb.r, rgb.g, rgb.b)

            return self._response_api(payload=payload)

        except Exception as e:
            self.logger.error(e)
            return self._response_api()

    async def get_color_name_rgb(self, request):
        """
        Function to get the color name by it's HEX code
            Args:
                request API request with r,g,b parameters query string

            Returns:
                web.Response
        """

        try:
            flag, err = await self._is_auth(headers=request.headers)
            if err:
                return web.HTTPForbidden(content_type=self.content_type,
                                         text=err)

            if [i for i in ['r', 'g', 'b'] if i not in request.query.keys()]:
                return self._response_api()

            r, g, b = int(request.query['r']), int(request.query['g']), int(request.query['b'])

            payload = self._get_payload(r, g, b)

            return self._response_api(payload=payload)

        except Exception as e:
            self.logger.error(e)
            return self._response_api()
