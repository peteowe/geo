from app.file.FileParser import FileParser
from app.file.exception.InvalidFileExtensionException import InvalidFileExtensionException

import bz2
from xml.etree import ElementTree

class GeoParser(FileParser):
  NO_VALUE = "<NO_VALUE>"
  logger = None
  fileExtension = None
  provider = None

  def __init__(self, logger, fileExtension, provider):
    self.logger = logger
    self.fileExtension = fileExtension.lower()
    self.provider = provider

  def parse(self, fileName): 
    if not fileName.lower().endswith(self.fileExtension):
      raise InvalidFileExtensionException("Invalid extension detected!")
    try:
      with bz2.BZ2File(fileName) as xml_file:
        parser = ElementTree.iterparse(xml_file, events=('end','start'))
        pipeline = self.provider.getBuffer()
        locations = {}
        id = ""
        isWay = False
        isHighway = False
        name = self.NO_VALUE
        type = self.NO_VALUE
        wayStart = False
        for events, elem in parser:
          if elem.tag == 'way' and events == 'end':
             if isHighway:
               for x, y in locations.items():
                 self.logger.log(name + " " + y + " " + type)
             id = ""
             isHighway = False
             locations.clear()
             name = self.NO_VALUE
             type = self.NO_VALUE
          if elem.tag == 'way' and events == 'start':
             if not wayStart:
               pipeline.execute()
               wayStart = True
             id = elem.attrib.get("id")
             isWay = True
          if elem.tag == 'tag' and events == 'start' and isWay:
             if elem.attrib.get("k") == 'highway':
               isHighway = True
             if elem.attrib.get("k") == 'name':
               name = elem.attrib.get("v")
               type = self.getType(name)

          if elem.tag == 'nd' and events == 'start' and isWay:
            asoc_id, coord = self.ndProcessing(elem)
            locations[asoc_id] = coord

          if elem.tag == "node" and events == 'start':
            self.nodeProcessing(elem, pipeline)
 
          elem.clear()  

    except Exception as e:
      raise e
  
  def nodeProcessing(self, elem, pipeline):
    nodeId = elem.attrib.get("id")
    lat = elem.attrib.get("lat")
    lon = elem.attrib.get("lon")
    pipeline.put({
      "hash": "temp",
      "key": nodeId,
      "value": lat + "," + lon
    })

  def ndProcessing(self, elem):
    nodeId = elem.attrib.get("ref")
    coordinates = self.provider.get({
        "hash": "temp",
        "key": nodeId
    })
    return nodeId, coordinates

  def getType(self, roadName):
    return roadName.split()[-1]
