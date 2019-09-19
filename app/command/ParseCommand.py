from app.command.Command import Command

class ParseCommand(Command):
  parser = None
  def __init__(self, parser):
    self.parser = parser
  def execute(self, args):
    if len(args) != 2:
      raise Exception("Must provide a filename")
    self.parser.parse(args[1])
