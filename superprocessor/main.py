
import subprocess as sp


def cmd(*args):

    stmt = []
    for arg in args:
        if ' ' in arg:
            stmt.extend(arg.split())
        else:
            stmt.append(arg)

    resp = sp.run(stmt,
                  capture_output=True,
                  text=True)

    return resp.stdout, resp.stderr or None


