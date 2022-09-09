import logging

logger = logging.getLogger('lab4')
# logger = logging.Logger("lab4")
# logger.setLevel(logging.INFO)

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)