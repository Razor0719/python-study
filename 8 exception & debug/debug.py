import logging

logging.basicConfig(level=logging.WARN)


def foo(s):
    n = int(s)
    logging.info(n)
    assert n != 0, logging.error('n is zero!')
    return 10 / n


def main():
    foo('0')


main()
