"""
Setup for integration tests - TODO
"""
import os
import logging

import pytest

TEST_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(TEST_DIR, 'data')


@pytest.fixture(scope="function")
def debug_caplog(caplog):
    """
    pytest capture log output at level=DEBUG
    """
    caplog.set_level(logging.DEBUG)
    return caplog
