from flask import Flask, Blueprint
from flask_cors import CORS
import discord
import os
from modules.utils.db import DBConnect
from modules.users.invite import InvitationSender

import asyncio
from modules.utils.config import Config
# from modules.utils.db import DBManager

from modules.utils.db import DBConnect, Base
from modules.utils.TokenManager import TokenManager
from modules.bot.discord_modules.bot import BotFork


# Prompt for credentials before initializing InvitationSender

# Instantiate the InvitationSender class with credentials


config = Config()

invitation_sender = InvitationSender(config.USERNAME, config.PASSWORD)
app = Flask("SoDA internal API", static_folder=None, template_folder=None)

# Initialize database connection
db_connect = DBConnect("sqlite:///./user.db")  # Adjust the URL to your database
app = Flask("SoDA internal API", static_folder=None, template_folder=None)
CORS(app)
tokenManger = TokenManager()
