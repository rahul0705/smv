"""
author: Rahul Mohandas
"""
import argparse
import logging

DEFAULT_PORT = 22


def main():
    #use a logger to make things easier for verbosity
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser()
    parser.add_argument('-P',
                        '--port',
                        type=int,
                        help="Specifies the port to connect to on the remote host.")
    parser.add_argument('-q',
                        '--quiet',
                        action="store_true",
                        help="Quiet mode.")
    parser.add_argument('-v',
                        '--verbose',
                        action='count',
                        default=0,
                        help="Verbose mode.")
    parser.add_argument('file1',
                        help="file1")
    parser.add_argument('file2',
                        help="file2")
    args = vars(parser.parse_args())
    #anything more than 2 v's would be considers 2 since that is debug logging
    if args["verbose"] > 2:
        args["verbose"] = 2
    args["verbose"] *= 10
    args["verbose"] = logging.WARNING - args["verbose"]
    if args["quiet"]:
        args["verbose"] = logging.ERROR
    logger.setLevel(args["verbose"])
    port = PORT
    if args["port"]:
        port = args["port"]
    logger.debug("using port %d", port)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
