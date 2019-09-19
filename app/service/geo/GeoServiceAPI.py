from app.service.geo.GeoService import GeoService
from app.service.geo.engine.GeoQueryEngine import GeoQueryEngine
from app.provider.elastic.ElasticProvider import ElasticProvider
from app.service.geo.exception.InvalidParameterException import InvalidParameterException
import settings as s

class GeoServiceAPI(GeoService):
  engine = None
  def __init__(self):
    provider = ElasticProvider(s.ELASTIC_HOST, s.ELASTIC_PORT)
    self.engine = GeoQueryEngine(provider)

  def getStats(self, radius, lat, lon):
    if radius == None or radius == "":
      raise InvalidParameterException("Invalid parameter provided")
    if lat == None or lat == "" or lon == None or lon == "":
      raise InvalidParameterException("Invalid parameter provided")
    try:
      float(lat)
      float(lon)
    except Exception:
      raise InvalidParameterException("Invalid parameter provided")
    return self.engine.getStats(radius, lat, lon)
