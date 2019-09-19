from app.provider.OperationBuffer import OperationBuffer

class RedisBuffer(OperationBuffer):
  pipeline = None
  mazSize = None
  size = None
  
  def __init__(self, pipeline, maxSize=1000):
    self.pipeline = pipeline
    self.maxSize = maxSize
    self.size = 0

  def put(self, hmap): 
    self.pipeline.hset(
      hmap.get("hash"),
      hmap.get("key"),
      hmap.get("value")
    )
    if(self.size >= self.maxSize):
      self.pipeline.execute()

  def execute(self): 
    self.pipeline.execute()
