class Config(object):
    LOGGER = false

    # Get this value from my.telegram.org/apps
    API_ID = "23053980"
    API_HASH = "9f7cb9215fa0007089951c86d31d0128"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://postgres:Aa7737057478@db.bnnujockqibqcykyshgi.supabase.co:5432/postgres"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://vedant12ok:vedant@cluster0.hknrwrr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/98bdc1e531232c5eda829.mp4"

    SUPPORT_CHAT = "jimiskamusic"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6409094763:AAGtnmvGV0NuoxpJg4IdxBAWXcMbX5n28zg"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5685358346  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
