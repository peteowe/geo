from app.logger.Logger import Logger

import logging
import os

class GeoLogger(Logger):
  logger = None
  def __init__(self, fileName):
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    logger = logging.getLogger('geo_logger')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(fileName,mode='a')
    formatter = logging.Formatter('%(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    self.logger = logger;

  def log(self, string): 
    self.logger.info(string)
