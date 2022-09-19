import logging
import sys

LOG_FORMAT = "%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s"
DATE_FORMAT = "%m-%d %H:%M"

logging.basicConfig(filename="app.log", level=logging.INFO, filemode="w",
                    format=LOG_FORMAT, datefmt=DATE_FORMAT)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT))

# logger = logging.getLogger("app")
_logger = logging.getLogger("localrun")
_logger.addHandler(stream_handler)

logger = _logger
