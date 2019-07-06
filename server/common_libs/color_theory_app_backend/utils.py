import os
import time
import logging
import argparse
from typing import Tuple, NamedTuple
from collections import namedtuple


def get_args_parser(PORT: int = 4500):
    """
    Extendable parser for input arguments

        Args:
            PORT: default port to be exposed
    """

    parser = argparse.ArgumentParser(add_help=True,
                                     description="Backend service API")
    parser.add_argument('-p', '--port',
                        help="Port to expose the API end-points",
                        default=PORT, type=int)

    parser.add_argument('-s', '--secrets',
                        help="Path to json with secrets",
                        default=None, type=str)

    return parser


def get_logger(log_path: str) -> logging.getLogger:
    """
    Initiate logger instance

        Args:
            log_path: str path to log files

        Returns:
            logger
    """

    if not os.path.isdir(log_path):
        os.makedirs(log_path)

    log_file = f"api_{time.strftime('%Y%m%d%H%M%S')}.log"

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=os.path.join(log_path, log_file),
                        filemode='a+')

    return logging.getLogger('logs')


# converted HEX2RGB
rgb = namedtuple('RGB', 'r g b')


def hex2rgb(hexcode: str) -> Tuple[NamedTuple('RGB', r=int, g=int, b=int), str]:
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

    return rgb(int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)), None
