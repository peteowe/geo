from app.command.DownloadCommand import DownloadCommand
from app.command.ParseCommand import ParseCommand
from app.command.DownloadParseCommand import DownloadParseCommand
from app.command.exception.InvalidCommandException import InvalidCommandException
from app.file.Downloader import Downloader
class CommandFactory:
  downloader = None
  parser = None
  def __init__(self, downloader, parser):
    self.downloader = downloader
    self.parser = parser
  def create(self, type):
    if type == 'download':
      return DownloadCommand(self.downloader)
    elif type == 'parse':
      return ParseCommand(self.parser)
    elif type == 'download_parse':
      return DownloadParseCommand(self.downloader, self.parser)
    raise InvalidCommandException("Invalid command provided")
