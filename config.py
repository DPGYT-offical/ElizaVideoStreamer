import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("BQFWDQ8AmixotvNC8eIyWK91sofgzyRjQswWHvuIOYSqxa_hvfInou7fwS1UAycDcvyXI9tUXbRihOl-Lin5f_dgXLirR4DiySil4YLAMQhqm8dfSKxustdxd2AT8aM1BlsPcC2e_S8sKB-BGxznjOqJgkLDted8l-LDYRN29NIHggrNhFvT1bCbZqfgCKMq4_KhavIRAgjR9Z1xiKF5TjhlyJxmNjrsfgVnQ8PyEXngO8OkjJERK8ZtYE6qen7I6px9GcTd8uk1W912uDc0YB4joN2vAthtwd6REAFRq5oKJPY1lPSw7bTGUk9fSzhWHb16QLOqWgYxGq1dB4G8bVu91ddZngAAAAF7nx57AA", "session")
BOT_TOKEN = getenv("6437947811:AAETguqBfMr-R0vN4QqFLsXp4j-q1D-x2uw")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("602443041994"))
API_HASH = getenv("e53eecba602443041994af39d029f3f6")
OWNER_NAME = getenv("OWNER_NAME", "dpgyt")
ALIVE_NAME = getenv("ALIVE_NAME", "dpgyt")
BOT_USERNAME = getenv("BOT_USERNAME", "dpgytbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "dpgyt")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "agentgost")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "INDIANBLACKHAT47")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/4104435ebaa2fdc591db1.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PereraSehath/Eliza-Annie-Video-Streamer")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/f529fa422259553b9a78f.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/89b7ca09f4b10e7ab117e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/b05b7f48a150177ac9d83.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/72cf9fc60847d67a7ee6a.jpg")
