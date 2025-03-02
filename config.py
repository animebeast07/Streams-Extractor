#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8181201051:AAHJ9ueGhalAL_mW4m81bi2LL_myV-mwA-Y")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "26169469"))
    API_HASH = os.environ.get("API_HASH", "1e2225f3d65b401d7d5bb921af531712")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5326198063").split())
    
