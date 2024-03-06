import os

from dotenv import load_dotenv

load_dotenv()

from logger import Logger
from utils import set_interval

Logger = Logger(os.getenv("HYPERDX_API_KEY"))

set_interval(Logger.info, 1)
