from app.provider.Provider import Provider
from app.provider.redis.RedisBuffer import RedisBuffer

import redis

class RedisProvider(Provider):
  redisClient = None
  def __init__(self, host, port):
    self.redisClient = redis.StrictRedis(
      host=host,
      port=port,db=0
    )
  def get(self, hmap): 
    data = self.redisClient.hget(
      hmap.get("hash"),
      hmap.get("key")
    )
    if data is not None:
      data = data.decode('utf-8')
    return data

  def put(self,hmap):
    self.redisClient.hset(
      hmap.get("hash"),
      hmap.get("key"),
      hmap.get("value")
    )
 
  def getBuffer(self): 
    return RedisBuffer(self.redisClient.pipeline())

  def delete(self,hmap): 
    return "DELETE"

  def update(self,hmap): 
    return "UPDATE"
