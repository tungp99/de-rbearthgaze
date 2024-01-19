__all__ = ["RawFlightSignal"]

from datetime import datetime
from typing import Optional

from munch import Munch


class RawFlightSignal(Munch):
    """
    Properties:

    """

    time: datetime
    icao24: str
    lat: Optional[float]
    lon: Optional[float]
    velocity: Optional[float]
    heading: Optional[float]
    vertrate: Optional[float]
    callsign: Optional[str]
    onground: bool
    alert: bool
    spi: bool
    squawk: Optional[str]
    baroaltitude: Optional[float]
    geoaltitude: Optional[float]
    lastposupdate: datetime
    lastcontact: datetime
