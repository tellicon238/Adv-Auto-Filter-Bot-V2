#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("11352440")

API_HASH = os.environ.get("0363a7c12ed2864e55f397c789097478")

BOT_TOKEN = os.environ.get("7219533594:AAEnnvwtIPIfpVeRoG1jdk-m0fUyWUZ6K5Y")

DB_URI = os.environ.get("mongodb+srv://Heizancs:heizan@tellicon.hpltxcm.mongodb.net/?retryWrites=true&w=majority&appName=Tellicon

USER_SESSION = os.environ.get("777000")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
