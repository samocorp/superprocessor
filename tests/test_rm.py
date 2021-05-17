
from tests import const


def test_rm():
    _, err = cmd('rm -rf ', const.DEFAULT_TEST_DIR)
    assert err is None


if __name__ == '__main__':
    test_rm()

