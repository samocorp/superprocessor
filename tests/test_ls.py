
from test import cmd as test_cmd


def test_ls():
    _, err = test_cmd('ls .')
    assert err is None


if __name__ == '__main__':
    test_ls()
