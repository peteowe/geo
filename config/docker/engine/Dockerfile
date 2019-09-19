FROM  ubuntu:18.04

LABEL maintainer="pkriadis@alumni.harvard.edu"

RUN apt-get update && apt-get install -y \
        python3.6 \
        python3-pip \
        curl

RUN ln -s /usr/bin/python3.6 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install Flask \
        requests \
        bz2file \
        geolib \
        redis \
        python-dotenv \
        elasticsearch \
        Flask-Caching
 
