from abc import ABC, abstractmethod
class QueryEngine(ABC):
  @abstractmethod
  def getStats(self, radius, lat, lon): 
    pass
