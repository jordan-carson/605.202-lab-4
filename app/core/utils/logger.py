import logging
import sys

LOG_FORMAT = "%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s"
DATE_FORMAT = "%m-%d %H:%M"

logging.basicConfig(filename="/Users/jordancarson/Projects/605.202-lab-4/app/logs/lab4.log", level=logging.INFO,
                    filemode="w", format=LOG_FORMAT, datefmt=DATE_FORMAT)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT))

_logger = logging.getLogger("lab4-local-run")
_logger.addHandler(stream_handler)
logger = _logger
