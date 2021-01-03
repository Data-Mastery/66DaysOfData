from typing import Tuple
import pandas as pd 

def func(a: int, b: int) -> int:
    return int


def func2(a: int, b: int) -> Tuple[int, int]:
    return a, b

func2.__annotations__
func2()


def concat_dfs(a: pd.DataFrame, b: pd.DataFrame, axis: int = 1) -> "2 gestackte DFs":
    '''
    Parameters
    ----------
    a : pd.DataFrame
        DESCRIPTION.
    b : pd.DataFrame
        DESCRIPTION.
    axis : int, optional
        DESCRIPTION. The default is 1. If you want to bind columns, use 1

    Returns
    -------
    pd.DataFrame
        concatenates two DataFrames and returns a new dataframe, concatenated by rows or columns, depending on the axis, which is 1 (column) by default.
    '''

    return pd.concat(a, b)

concat_dfs()