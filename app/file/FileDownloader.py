from abc import ABC, abstractmethod
class FileDownloader(ABC):
  @abstractmethod
  def download(self, url, fileName): 
    pass
