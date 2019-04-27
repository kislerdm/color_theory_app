import pandas as pd
from typing import Tuple
import pickle


def read_object(filename: str):
    """
    Function to read/un-pickle python object

        Args:
            filename: str path to pickle file
    """

    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    return obj


class Predict:
    """
    Class to predict warm/cool class of the color
    """

    def __init__(self, logger, path_model: str):
        """
            Args:
                path_model: str path to pickled model
        """
        self.logger = logger
        # read pretrained model
        self.model = read_object(path_model)

    @classmethod
    def _inpt2df(self, r: int, g: int, b: int) -> pd.DataFrame:
        """
        Convert input RGB params into pd.DataFrame

            Args:
                RGB color code
                r: int
                g: int
                b: int

            Returns:
                pd.DataFrame
        """

        return pd.DataFrame({'r': [r], 'g': [g], 'b': [b]})

    def get_class(self, r: int, g: int, b: int, model=None) -> Tuple[int, str]:
        """
        Function to predict the color class based on
            Args:
                RGB color code:
                    r: int
                    g: int
                    b: int

                model classifier model

            Returns:
                pd.DataFrame
        """

        try:
            m = self.model
            if model:
                m = model

            dat = self._inpt2df(r, g, b)

            prediction = m.predict(dat)

            return int(prediction.squeeze()), None

        except Exception as err:
            self.logger.error(err)
            return None, err
