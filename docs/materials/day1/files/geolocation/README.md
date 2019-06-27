Worker Node Geolocation
=======================

The contents of this repository are for the OSG User School Day 2 worker node (WN) geolocation exercises.
It contains the following:

- **data/** - GeoLite2 city database from [MaxMind](https://dev.maxmind.com/geoip/geoip2/geolite2/)
- **src/** - The `wn-geoip` library for returning lat/long coordinates from worker nodes in the CHTC pool and CEs out on
  the OSG.
  It also contains the [geoip2](https://pypi.org/project/geoip2/) pip module and its requirements, installed with:

    ```
    pip install --ignore-installed --no-compile --target src/ geoip2
    ```
