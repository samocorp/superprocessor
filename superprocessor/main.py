
import subprocess as sp
from typing import (
    Union, Tuple
)


def cmd(* args: str) -> Tuple[str, Union[str, None]]:

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


