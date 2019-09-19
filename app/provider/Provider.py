from abc import ABC, abstractmethod
class Provider(ABC):
  @abstractmethod
  def get(self, hmap): 
    pass

  @abstractmethod
  def put(self,hmap): 
    pass
 
  @abstractmethod
  def delete(self,hmap): 
    pass

  @abstractmethod
  def update(self,hmap): 
    pass

  @abstractmethod
  def getBuffer(self): 
    pass
