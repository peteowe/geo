from app.command.Command import Command

class DownloadCommand(Command):
  downloader = None
  def __init__(self, downloader):
    self.downloader = downloader
  def execute(self, args):
    if len(args) != 3:
      raise Exception("Must provide a filename and url to continue")
    self.downloader.download(args[2],args[1])
