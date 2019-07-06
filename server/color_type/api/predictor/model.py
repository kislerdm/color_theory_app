from typing import Tuple, Any
import pandas as pd
import numpy as np
import pickle


def get_model(path: str) -> Tuple[Any, str]:
    """
    Function to read the model object with the method predict

        Args:
            path: str path to the model

        Returns:
            tuple of model object, error str
    """

    model, err = read_model(path)
    if err:
        return None, err

    if 'predict' not in model.__dir__():
        return None, f"Model in {path} doesn't have predict method"

    return model, err


def read_model(path: str) -> Tuple[Any, str]:
    """
    Function to read model

        Args:
            path: str path to the model as pickle

        Returns:
            tuple of model object, error str
    """
    try:
        with open(path, 'rb') as f:
            model = pickle.load(f)
        return model, None

    except Exception as err:
        return None, err


class model_baseline:
    """
    Baseline model
    """

    def predict(X: pd.DataFrame) -> np.array:
        """
        Function to run a base line prediction

            Args:
                X: input data

            Returns:
                array
        """
        def _rule(row: pd.DataFrame) -> int:
            """
            Model rule
                Args:
                    Row: pd.DataFrame row

                Return:
                    int
            """

            if row['r'] > row['g'] > row['b']:
                return 1

            return 0

        return X.apply(lambda row: _rule(row), axis=1)
