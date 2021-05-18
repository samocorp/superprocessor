
import subprocess as sp
from typing import (
    Union, Tuple
)

"""
Samo c 2021
Author: Samoto
"""


def cmd(* args: str) -> Tuple[str, Union[str, None]]:
    """

    :param args: list of strings --
        to be concatenated into stmt
    :return: tuple --
        of length 2: std (output, error)
    """

    if not args:
        return tuple()

    stmt: [str] = []
    for arg in args:
        if ' ' in arg:
            stmt.extend(arg.split())
        else:
            stmt.append(arg)

    resp = sp.run(stmt,
                  capture_output=True,
                  text=True)

    return resp.stdout, resp.stderr or None
