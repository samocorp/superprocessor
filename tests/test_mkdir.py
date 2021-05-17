
from superprocessor import cmd
from tests import const


def test_mkdir():
    _, err = cmd('mkdir', const.DEFAULT_TEST_DIR)
    assert err is None


if __name__ == '__main__':
    test_mkdir()
