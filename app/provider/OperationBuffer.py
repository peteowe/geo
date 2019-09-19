from abc import ABC, abstractmethod
class OperationBuffer(ABC):
  @abstractmethod
  def put(self, hmap): 
    pass

  @abstractmethod
  def execute(self): 
    pass
 
