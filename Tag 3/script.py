from typing import Tuple

def func(a: int, b: int) -> Tuple[int, int]:
    return a, b

func.__annotations__


func()