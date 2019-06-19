import json
from aiohttp import web
from color_theory_app_backend_libs.utils import hex2rgb


class EndPoints:
    """
    Class for API endpoints
    """

    def __init__(self,
                 logger,
                 predictor,
                 secrets: dict = None,
                 content_type: str = 'applicaiton/json', ):
        """
            Args:
                logger: logging instance
                predictor: model with predict method
                secrets: dict with accepted APIKEYS
                content_type: API response type
        """

        self.content_type = content_type
        self.logger = logger
        self.predictor = predictor
        self.secrets = secrets

    def _response_api(self, payload=None) -> web.Response:
        """
        Function to build the endpoint response

        Args:
            payload: array/dict to return on API call

        Returns:
            web.Response
        """

        if not payload:
            return web.Response(body=json.dumps({"data": None}),
                                status=500,
                                content_type=self.content_type)

        return web.Response(body=json.dumps(payload),
                            status=200,
                            content_type=self.content_type)

    def _get_payload(self, r: int, g: int, b: int) -> dict:

        prediction, err = self.predictor.get_class(r, g, b)

        if err:
            return None

        return {'data': {
                        "color": {'r': r, 'g': g, 'b': b},
                        'is_warm': prediction
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

        if self.secrets is None:
            return True, None

        if headers.get('APIKEY') is None:
            return False, "No APIKEY provided"

        if headers.get('APIKEY') not in self.secrets.values():
            return False, "Wrong APIKEY provided"

        return True, None

    async def get_color_cat_rgb(self, request):
        """
        Function to predict the color category; 1 - warm, 0 - cool

            Args:
                request with r,b,g parameters

            Returns:
                int
        """

        try:
            flag, err = await self._is_auth(headers=request.headers)
            if err:
                return web.HTTPForbidden(content_type=self.content_type,
                                         text=err)

            if [i for i in ['r', 'g', 'b'] if i not in request.query.keys()]:
                return self._response_api()

            r, g, b = int(request.query['r']), \
                int(request.query['g']), \
                int(request.query['b'])

            payload = self._get_payload(r, g, b)

            return self._response_api(payload=payload)

        except Exception as e:
            self.logger.error(e)
            return self._response_api()

    async def get_color_cat_hex(self, request):
        """
        Function to predict the color category; 1 - warm, 0 - cool

            Args:
                request with HEX parameter string

            Returns:
                int
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
