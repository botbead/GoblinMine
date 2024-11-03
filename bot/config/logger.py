import sys

from loguru import logger

logger.remove()

logger_str_format = (
    "<white>[⚔]</white> | "
    "<c><b>{extra[session_name]: <7}</b></c> | "
    "<white><b>{message}</b></white>"
)
logger.add(sink=sys.stdout, format=logger_str_format, colorize=True)
log = logger.bind(session_name="GLOBAL").opt(colors=True)
