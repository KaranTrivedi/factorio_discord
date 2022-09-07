#!./venv/bin/python

"""
Docstring should be written for each file.
run `pylint filename.py` to find recommendations on improving format.
"""

import configparser
import json
import logging
import sys

import factorio_rcon

#Define config and logger.
CONFIG = configparser.ConfigParser()
CONFIG.read("conf/config.ini")
SECTION = "factorio_discord"

logger = logging.getLogger(SECTION)

class Factorio_discord:
    """
    Create sample class
    """

    def __init__(self, var):
        self.var = var

    def __str__(self):
        """
        stringify
        """

        return json.dumps(vars(self), indent=2)


def main():
    """
    Main function.
    """

    logging.basicConfig(filename=CONFIG[SECTION]["log"],
                    level=CONFIG[SECTION]["level"],
                    format="%(asctime)s::%(name)s::%(funcName)s::%(levelname)s::%(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

    logger.info("####################STARTING####################")

    passw = CONFIG[SECTION]["passw"]
    factor = sys.argv[1]

    # client = factorio_rcon.RCONClient("192.168.0.16", 27015, passw)
    client = factorio_rcon.RCONClient("127.0.0.1", 27015, passw)
    #response = client.send_command("/help")
    response = client.send_command(f'/c game.speed={factor}')

    print(response)

if __name__ == "__main__":
    main()
