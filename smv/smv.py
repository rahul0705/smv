"""
author: Rahul Mohandas
"""
import argparse
import logging


def main():
    #use a logger to make things easier for verbosity
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose',
                        '-v',
                        action='count',
                        default=0,
                        help="level of verbosity")
    args = vars(parser.parse_args())
    if args["verbose"] > 3:
        args["verbose"] = 3
    args["verbose"] *= 10
    logger.setLevel(logging.ERROR - args["verbose"])
    logger.error("error")
    logger.warn("warn")
    logger.info("info")
    logger.debug("debug")

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
