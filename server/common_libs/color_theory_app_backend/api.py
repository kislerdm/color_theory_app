import logging
from typing import Dict, Any
from aiohttp import web
from abc import ABC, abstractmethod
from .utils import hex2rgb


class EndPoints(ABC):
    """
    Base class for backend services endpoints

        Args:
            logger: logging instance
            secrets: dict with accepted APIKEYS
            content_type: API response type
    """

    logger: logging.getLogger()
    secrets: Dict[str, Any]
    content_type: str
    payload_key: str

    def __init__(self):
        self.content_type = 'applicaiton/json'
        self.logger = logging.getLogger('log')
        self.secrets = {}
        self.payload_key = 'value'

    async def is_auth(self, headers) -> web.Response:
        """
        Function to test client authenticaiton
            Args:
                headers: request API headers dict

            Returns:
                web.Response
        """

        if len(self.secrets) == 0:
            return True, None

        if headers.get('APIKEY') is None:
            return False, "No APIKEY provided"

        if headers.get('APIKEY') not in self.secrets.values():
            return False, "Wrong APIKEY provided"

        return True, None

    @abstractmethod
    def predictor(self, r: int, g: int, b: int) -> Any:
        """
        Generic function to predict value on input RGB color
        """
        pass

    def get_payload(self, r: int, g: int, b: int) -> dict:
        """
        Function to define API response payload

            Args:
                r,g,b: int, color RGB encoding

            Return:
                dict
        """

        prediction, err = self.predictor(r, g, b)

        if err:
            return None

        payload = {'data': {
                    "color": {'r': r, 'g': g, 'b': b}
                    }
                   }
        payload['data'][self.payload_key] = prediction

        return payload

    def response_api(self, payload=None) -> web.Response:
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

    async def on_hex(self, request):
        """
        Function to get the color name by it's HEX code

            Args:
                request API request with HEX parameter query string

            Returns:
                web.Response
        """

        try:
            flag, err = await self.is_auth(headers=request.headers)
            if err:
                return web.HTTPForbidden(content_type=self.content_type,
                                         text=err)

            if "hexcode" not in request.query.keys():
                return self.response_api()

            hexcode = request.query['hexcode']
            rgb, err = hex2rgb(hexcode)

            if err:
                self.logger.error(err)
                return self.response_api()

            payload = self.get_payload(rgb.r, rgb.g, rgb.b)

            return self.response_api(payload=payload)

        except Exception as err:
            self.logger.error(err)
            return self.response_api()

    async def on_rgb(self, request):
        """
        Function to get the color name by it's HEX code

            Args:
                request API request with r,g,b parameters query string

            Returns:
                web.Response
        """

        try:
            flag, err = await self.is_auth(headers=request.headers)
            if err:
                return web.HTTPForbidden(content_type=self.content_type,
                                         text=err)

            if [i for i in ['r', 'g', 'b'] if i not in request.query.keys()]:
                return self.response_api()

            r, g, b = int(request.query['r']), int(request.query['g']), int(request.query['b'])

            payload = self.get_payload(r, g, b)

            return self.response_api(payload=payload)

        except Exception as err:
            self.logger.error(err)
            return self.response_api()
