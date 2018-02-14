import logging
from paths import PROJECT_ROOT
import os
from ConfigFilesLoader import logger_name

## setting up logger
log = logging.getLogger(logger_name)
log.setLevel(logging.INFO)
debug_handler = logging.handlers.RotatingFileHandler(os.path.join(PROJECT_ROOT, "logs"), mode='a', maxBytes=4096 * 1024, backupCount=5)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(funcName)s (%(lineno)s) [%(levelname)s] %(message)s')
plain_formatter = logging.Formatter('%(message)s')

debug_handler.setFormatter(formatter)
console_handler.setFormatter(plain_formatter)

log.addHandler(debug_handler)
log.addHandler(console_handler)
