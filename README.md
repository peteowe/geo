# Geolocation Project

## Purpose

The purpose of the project is to provide users the possibility of viewing the most popular street names and types.


## Utilized Software

The following software is used by the project:

* Python 3.6
* Elasticsearch 6.3.1
* Logstash 6.3.1
* Filebeat 6.3.1
* Redis 5.0.5
* Flask 1.1.1
* Docker 17.06
* Docker-compose 1.15

## Installation

To run the geolocation project docker and docker-compose must be installed, the following commands must be made:


``` sh
docker-compose up -d

```

Elasticsearch must be ready to receive commands before executing. Please verify logs to see if elasticsearch is ready with the following command:

``` sh
docker-compose logs geoelasticsearch

```

The following commands will load the necessary mapping template and create the required 'geo' index:

``` sh
docker-compose exec engine bash
cd config/docker/elasticsearch/
curl -XPUT -H 'Content-Type: application/json' http://geoelasticsearch:9200/_template/geo_template?pretty -d @geo_map_template.json
curl -XPUT http://geoelasticsearch:9200/geo?pretty

```

When elasticsearch is ready, we can begin loading data into the system. The system can only ingest compressed osm documents with a file extension of bz2. Please run the following command to download and parse the document.

The following command are available:


``` sh
download
parse
download_parse

```

To download and parse a document you can the following commands

``` sh
docker exec -it python_engine bash
python Importdata.py download_parse test.bz2 https://download.geofabrik.de/north-america/us/new-mexico-latest.osm.bz2
```

When all the required data has been inputed into elasticsearch, a browser can be opened to see the availble derived data. The following url can be used to navigate the data.

``` sh
http://localhost:5000
```

To view the most popular street names and types, please provide with the necessary latitude and longitude coordinates and radius in kilometers.

Below is a picture of how the page looks like.

![Preview Pic](https://github.com/peteowe/geo/blob/master/image/demo.jpg)
