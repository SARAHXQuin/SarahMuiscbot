import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29906518"))
API_HASH = getenv("API_HASH", "76a9e84e87200fb7311a2d779a42d13a")

BOT_TOKEN = getenv("BOT_TOKEN", "6111967692:AAFEXQo6_5LyA9GNJz-m233iS_57eWr1aBk")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://avianandh004:sxptcTvwrszpdVF7@cluster0.op7ylmt.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001975396715"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Sarah")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6140142325 1556830659").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY") 
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SARAHXQuin/SarahMuiscbot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/SARAHXQuin/SarahMuiscbot")
GIT_TOKEN = getenv("GIT_TOKEN", "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" )

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sarah_updates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AF_Support_Group")


AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", True)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQASt43FNLgo6GHz-wDmXTdzO1jLR_o89T2XX0M_GoHVIGA6JlG3LkIYZl9o4UXTt7mnu_J9a9sn_d_vzHZNLSBey9W3JDgr4lb1s6oR2PLjtNyvC2c3FHSdhi3C3908K0CDIee9PGJG5smK8kC64ShNQaXMftUrlJtcCadFskmRYBTrqKh5v8k19Qkd18iDAxc3PJ3pYu9OzWS4OV-jycTHt36IbenXpxXhjlpXFyb68r0ePRX5-b_iy0CY2Av6MrqlE5LhJHLFWoV6nYMbCfFYuK_cgtHnMlaxrO5tpBN6MiJqFMM71FowVSqVAFHBVuk9tcNnDeIFJLHeL2lJIKLgAAAAAW37IvUA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/87c57ca975e1c1a71deaf.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/86a7ff0f5d480f255fafb.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/6054be6dbfc0f654db62b.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/cd427bd0b41314bc99bc1.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/87c57ca975e1c1a71deaf.jpg"
