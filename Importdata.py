from app.provider.redis.RedisProvider import RedisProvider
from app.command.CommandFactory import CommandFactory
from app.file.Downloader import Downloader
from app.logger.GeoLogger import GeoLogger
from app.file.GeoParser import GeoParser

import sys
import settings as s

def commandProcessing(argv):
  argv.pop(0)
  if len(argv) <= 0:
    raise Exception("Invalid parameters detected")
  downloader = Downloader()
  logger = GeoLogger(s.LOG_FILE)
  provider=RedisProvider(s.REDIS_HOST,s.REDIS_PORT)
  command = argv[0].lower()
  parser = GeoParser(logger,s.FILE_EXTENSION,provider)
  factory = CommandFactory(downloader,parser)
  factory.create(command).execute(argv)
  pass

try:
  commandProcessing(sys.argv)
except Exception as e:
  print(e)
