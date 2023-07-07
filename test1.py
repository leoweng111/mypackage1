# This is a simple test for launching local package.

import datetime


def test(name):
    """
    A test func.

    :param name: name of the tester
    :return: none
    """
    print(f'Hello, the package has been launched successfully by {name} at {datetime.datetime.now()}')

