from aiohttp import web
from typing import Tuple


PORT = 4500


async def model(r: int, g: int, b: int) -> Tuple[int, str]:
    """ Baseline model
    
        Args:
          r,g,b: RGB color code
        
        Returns:
          colot type int
    """
    try:
      if r > g > b:
        return 1, None
      else:
        return 0, None
      
    except Exception as ex:
      return None, ex
  
async def onRGB(request):
    """ Function to get the color type on RGB code
        
        Args:
          request: web.Request with rgb color code
         
        Returns:
          web.json_response  
    """
    
    if [i for i in ['r', 'g', 'b'] if i not in request.query.keys()]:
      return web.json_response({"data": None},
                               status=web.HTTPBadRequest().status_code)
    
    r, g, b = tuple([int(request.query[i]) for i in ['r', 'g', 'b'] if i in request.query.keys()])
    is_warm, err = await model(r, g, b)
    if err:
        web.json_response({"data": None},
                          status=web.HTTPInternalServerError().status_code)
    
    return web.json_response({"data": {
                                  "color": {
                                      "r": r,
                                      "g": g,
                                      "b": b
                                  },
                                  "is_warm": is_warm}
                              },
                             status=web.HTTPOk().status_code)

async def onHEX(request):
    """ Function to get the color type on RGB code
        
        Args:
          request: web.Request with rgb color code
         
        Returns:
          web.json_response  
    """
    
    if [i for i in ['hexcode'] if i not in request.query.keys()]:
      return web.json_response({"data": None},
                               status=web.HTTPBadRequest().status_code)

    def _hex2rgb(hexcode: str) -> Tuple[tuple, str]:
        """
        Function to convert HEX to RGB color code

            Args:
                hexcode: string HEX color code

            Returns:
                tuple of named tuple of (r,g,b) -> (int,int,int) and error str
        """
        hex = hexcode.replace('#', '')
        if len(hex) != 6:
            return None, 'Wrong HEX format'

        return (int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)), None
  
    (r, g, b), err = _hex2rgb(request.query['hexcode'])
    if err:
        web.json_response({"data": None},
                          status=web.HTTPInternalServerError().status_code)
        
    is_warm, err = await model(r, g, b)
    if err:
        web.json_response({"data": None},
                          status=web.HTTPInternalServerError().status_code)

    return web.json_response({"data": {
                                  "color": {
                                      "r": r,
                                      "g": g,
                                      "b": b
                                  },
                                  "is_warm": is_warm}
                              }, 
                             status=web.HTTPOk().status_code)
    
if __name__ == "__main__":
    app = web.Application()
    app.router.add_get('/rgb', onRGB)
    app.router.add_get('/hex', onHEX)
    web.run_app(app, port=PORT)
 
