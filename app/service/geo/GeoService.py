from abc import ABC, abstractmethod
class GeoService(ABC):
  @abstractmethod
  def getStats(self, radius, lat, lon): 
    pass
