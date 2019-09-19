from app.provider.Provider import Provider

from elasticsearch import Elasticsearch


class ElasticProvider(Provider):
  elastic = None
  def __init__(self, host, port):
    self.elastic = Elasticsearch(
      host + ":" + str(port)
    )

  def get(self, hmap):
    body = hmap.get("body")
    tag = hmap.get("tag")
    a = self.elastic.search(index="geo", body=body)['aggregations'][tag]['buckets']
    return a

  def put(self,hmap):
    pass
 
  def getBuffer(self): 
    pass

  def delete(self,hmap): 
    pass

  def update(self,hmap): 
    pass
