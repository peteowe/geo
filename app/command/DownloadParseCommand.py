from app.command.Command import Command
from app.command.DownloadCommand import DownloadCommand
from app.command.ParseCommand import ParseCommand

class DownloadParseCommand(Command):
  downloader = None
  parser = None
  def __init__(self, downloader, parser):
    self.downloader = downloader
    self.parser = parser
  def execute(self, args):
    if len(args) != 3:
      raise Exception("Must provide a filename and url to continue")
    DownloadCommand(self.downloader).execute(args)
    ParseCommand(self.parser).execute(args[:2])
