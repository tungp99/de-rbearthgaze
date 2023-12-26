__all__ = ["RawFlight"]

from datetime import datetime
from typing import Optional

from munch import Munch


class RawFlight(Munch):
    """
    Properties:

    """

    reference_timestamp: datetime
    timestamp: datetime
    aprs_type: str
    beacon_type: str
    aircraft_type: str
    name: str
    dstcall: str

    relay: Optional[str]
    receiver_name: str
    symbolcode: str
    symboltable: str
    latitude: str
    longitude: str
    altitude: str
    track: str
    ground_speed: str
    address_type: str
    stealth: str
    address: str
    climb_rate: str

    gps_quality_vertical: Optional[int]
    gps_quality_horizontal: Optional[int]

    climb_rate: Optional[int]
    turn_rate: Optional[float]
    flightlevel: Optional[float]
    signal_quality: Optional[float]
    error_count: Optional[int]
    frequency_offset: Optional[float]

    software_version: Optional[float]
    hardware_version: Optional[int]
    real_address: Optional[str]
    signal_power: Optional[float]
    proximity: Optional[str]
