__all__ = ["RawAirport"]

from typing import Optional

from munch import Munch


class RawAirport(Munch):
    """
    Properties:
        `icao`      ICAO 4-letter DOC7910 Location Indicator or (if none) an internal Pseudo-ICAO Identifier [1] (28,133 entries) \n
        `iata`      IATA 3-letter Location Code (7,588 entries) or an empty string [2] \n
        `name`      Official name (latin script) \n
        `city`      City in latin script, ideally using the local language \n
        `subd`      Subdivision (e.g. state, province, region, etc.), ideally using the local-language or English names of ISO 3166-2 \n
        `country`   ISO 3166-1 alpha-2 country code (plus XK for Kosovo) \n
        `elevation` MSL elevation (the highest point of the landing area) in feet; it is often wrong \n
        `lat`       Latitude (decimal) \n
        `lon`       Longitude (decimal) \n
        `tz`        Timezone expressed as a tz database name (IANA-compliant) or an empty string for Antarctica \n
        `lid`       U.S. FAA Location Identifier (12,567 entries), or an empty string \n
    """

    icao: str
    iata: Optional[str]
    name: str
    city: str
    subd: str
    country: str
    elevation: str
    lat: float
    lon: float
    tz: str
    lid: str
