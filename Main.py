from flask import Flask
from flask_caching import Cache
from flask import abort
from flask import request
from flask import jsonify
from flask import render_template
from app.service.geo.GeoServiceAPI import GeoServiceAPI

import settings as s

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': s.REDIS_FULL_URL})
service = GeoServiceAPI()

@app.route('/',methods=['GET'])
def page():
  try:
    radius = request.args.get('radius')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    data = None
    if radius is None or lat is None or lon is None:
      return render_template('page.html', data = data)
    data = service.getStats(radius, lat, lon)
    return render_template('page.html', data = data, radius=radius, lat=lat, lon=lon)
  except Exception:
    abort(400)

@app.route('/api/v1/stats/',methods=['GET'])
@cache.memoize(300)
def stats():
  try:
    radius = request.args.get('radius')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return jsonify(service.getStats(radius, lat, lon))
  except Exception:
    abort(400)
