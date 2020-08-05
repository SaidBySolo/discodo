# -*- coding: utf-8 -*-

__title__ = "discodo"
__author__ = "kijk2869"
__lisence__ = "MIT"
__version__ = "0.1.0a"

from collections import namedtuple

from .AudioSource import *
from .gateway import VoiceSocket
from .manager import AudioManager
from .natives import *
from .node import *
from .player import Player
from .stat import getStat
from .updater import check_version
from .utils import *
from .voice_client import VoiceClient
from .voice_connector import VoiceConnector

try:
    import discord
except ModuleNotFoundError:
    pass
else:
    from .DPYClient import DPYClient

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")

version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel="alpha", serial=0)
