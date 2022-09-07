#!./venv/bin/python

"""
Simple python discord bot to talk to factorio RCON server
"""

import discord
import configparser
import json
import logging

import factorio_rcon

#Define config and logger.
CONFIG = configparser.ConfigParser()
CONFIG.read("conf/config.ini")
SECTION = "factorio_discord"
RCON_PASS = CONFIG[SECTION]["passw"]
DISC_TOKEN = CONFIG[SECTION]["token"]

logger = logging.getLogger(SECTION)

intents = discord.Intents.default()
intents.message_content = True

disc_client = discord.Client(intents=intents)
factorio_client = factorio_rcon.RCONClient("127.0.0.1", 27015, RCON_PASS)

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

@disc_client.event
async def on_ready():
    logger.info(f'We have logged in as {disc_client.user}')

@disc_client.event
async def on_message(message):

    if message.author == disc_client.user:
        return

    if message.content.startswith('/c'):

        factorio_client = factorio_rcon.RCONClient("127.0.0.1", 27015, RCON_PASS)

        await message.channel.send('Executing command..')
        response = factorio_client.send_command(f'{message.content}')
        await message.channel.send(f"Reply from factorio server: {response}")


def main():
    """
    Main function.
    """

    logging.basicConfig(filename=CONFIG[SECTION]["log"],
                    level=CONFIG[SECTION]["level"],
                    format="%(asctime)s::%(name)s::%(funcName)s::%(levelname)s::%(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

    logger.info("####################STARTING####################")

    disc_client.run(DISC_TOKEN, log_handler=None)

if __name__ == "__main__":
    main()
