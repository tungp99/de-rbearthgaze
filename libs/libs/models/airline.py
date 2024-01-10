__all__ = ["RawAirline"]

from typing import Literal, Optional

from munch import Munch


class RawAirline(Munch):
    """
    Properties:
        `name`      Name of the airline. \n
        `alias`     Alias of the airline. ex, All Nippon Airways is commonly known as "ANA". \n
        `icao`      2-letter IATA code, if available. \n
        `iata`      3-letter ICAO code, if available. \n
        `callsign`  Airline callsign. \n
        `country`   Country or territory where airport is located. See Countries to cross-reference to ISO 3166-1 codes. \n
        `active`    "Y" if the airline is or has until recently been operational, "N" if it is defunct. This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as "Y". \n
    """

    name: str
    alias: Optional[str]
    icao: Optional[str]
    iata: Optional[str]
    callsign: Optional[str]
    country: str
    active: Literal["Y", "N"]
