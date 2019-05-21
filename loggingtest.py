"""
Test the logging module using quadratic formula:
"""
import logging
import math
import pytest


class CalculateError(Exception):
    pass


LOG_LEVEL = logging.DEBUG

logging.basicConfig(filename="C:\\Users\\User\\PycharmProjects\\daily_python_practice\\log\\loggingtest.log",
                    filemode="w",
                    level=LOG_LEVEL,
                    format="[%(asctime)s]-[%(levelname)s] %(message)s")
logger = logging.getLogger()


def quadratic_formula(a, b, c):
    """return solution to equation: a*x^2 + b*x + c = 0"""
    logger.info("quadratic_formula(%s, %s, %s)" % (a, b, c))

    #compute discriminant: b^2 - 4*a*c
    logger.debug("compute discriminant: b^2 - 4*a*c")
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        logger.critical("discriminant = %f, it has to be greate or equal to 0" % (discriminant))
        raise CalculateError("b^2 - 4*a*c has to be greater or equal to 0")
    else:
        #compute two roots
        logger.debug("compute two roots")
        root1 = (-1*b + math.sqrt(discriminant)) / (a*2)
        root2 = (-1*b - math.sqrt(discriminant)) / (a*2)

        return root1, root2


def test_normal():
    r1, r2 = quadratic_formula(1, 0, -4)
    print(r1, r2)
    assert r1,r2 == (2, -2)


def test_exception():
    with pytest.raises(CalculateError) as ce:
        r1, r2 = quadratic_formula(1, 2, 6)
    print(ce.value)
    assert str(ce.value) == "b^2 - 4*a*c has to be greater or equal to 0"


if __name__ == "__main__":
    test_normal()
    test_exception()

