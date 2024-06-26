import pytest
from utilities.customLogger import LogGen


def test_logging():
    logger = LogGen.loggen()

    logger.info("This is an info message")
    logger.debug("This is a debug message")
    logger.error("This is an error message")

    assert True
