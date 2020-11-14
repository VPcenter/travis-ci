import sys

from loguru import logger

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD в HH:mm:ss}</green> | <cyan>{level}</cyan> | {message}")

logger.debug("That's it, beautiful and simple logging!")