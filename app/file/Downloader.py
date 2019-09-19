from app.file.FileDownloader import FileDownloader

import requests
import shutil

class Downloader(FileDownloader):
  LENGTH = 1000000
  def download(self, url, fileName): 
    with requests.get(url, stream=True) as r:
      with open(fileName, 'wb') as f:
        shutil.copyfileobj(r.raw, f,length = self.LENGTH)
