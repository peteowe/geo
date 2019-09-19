from app.service.geo.engine.QueryEngine import QueryEngine

class GeoQueryEngine(QueryEngine):
  provider = None
  SIZE = 20
  def __init__(self, provider):
    self.provider = provider

  def getStats(self, radius, lat, lon):
    statsBody = self.getStatsBody(radius,lat,lon)
    typesBody = self.getTypesBody(radius,lat,lon)
    streets = {"roadNames": self.provider.get({"body": statsBody, "tag": "streets"})}
    types = {"roadTypes":self.provider.get({"body": typesBody, "tag": "types"})}
    data = {}
    data['streets'] = self.formatData(streets, "roadNames")
    data['types'] = self.formatData(types, "roadTypes")
    #data['roadTypes'] = self.formatData(types)
    return data
  def getStatsBody(self, radius, lat, lon):
    body = {
      "aggs" : {
        "streets" : {
          "terms" : { "field" : "streetName.keyword", "size" : self.SIZE },
        }
      },
      "query":{
        "bool":{
          "must_not": {
            "term" : {
              "streetType.keyword" : "<NO_VALUE>"
            }
          },
          "filter":{
            "geo_distance":{
              "distance": str(radius) + "km",
              "pin.location":{
                "lat":lat,
                "lon":lon
              }
            }
          }
        }
      }
    }
    return body

  def getTypesBody(self, radius, lat, lon):
    body = {
      "aggs" : {
        "types" : {
          "terms" : { "field" : "streetType.keyword", "size" : self.SIZE }
        }
      },
      "query":{
        "bool":{
          "must":{
            "match_all" : {}
          },
          "must_not": {
            "term" : {
              "streetType.keyword" : "<NO_VALUE>"
            }
          },
	  "filter":{
	    "geo_distance":{
	      "distance": str(radius) + "km",
	      "pin.location":{
                "lat":lat,
	        "lon":lon
	      }
	    }
	  }
        }
      }
    }
    return body

  def formatData(self, data, key):
    v = []
    l = []
    for value in data[key]:
      v.append(value['key'])
      l.append(value['doc_count'])
    data['lables'] = v
    data['values'] = l
    return data
