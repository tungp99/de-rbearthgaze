__all__ = ["RawAircraft"]

from typing import Iterable, Optional

from munch import Munch


class RawAircraft(Munch):
    """
    Properties:
        icao                ICAO 4 letters \n
        classification       \n
        category             \n
        manufacturers        \n
        wing_span           Wing Span (m) \n
        length              Length (m) \n
        height              Height (m) \n
        mtow                MTOW (t) \n
        fuel_capacity       Fuel Capacity (ltr) \n
        maximum_range       Maximum Range (Nm) \n
        persons_on_board    Persons On Board \n
        take_off_distance   Take Off Distance (m) \n
        landing_distance    Landing Distance (m) \n
        absolute_ceiling    Absolute Ceiling (x100ft) \n
        optimum_ceiling     Optimum Ceiling (x100ft) \n
        maximum_speed       Maximum Speed (kts/M) \n
        optimum_speed       Optimum Speed (kts/M) \n
        maximum_climb_rate  Maximum Climb Rate (ft/min) \n
    """

    img_3d: str
    img_cs: str

    icao: str
    classification: str
    category: str
    manufacturers: Iterable[str]
    wing_span: Optional[float]
    length: Optional[float]
    height: Optional[float]
    mtow: Optional[float]
    fuel_capacity: Optional[int]
    maximum_range: Optional[int]
    persons_on_board: Optional[int]
    take_off_distance: Optional[int]
    landing_distance: Optional[int]
    absolute_ceiling: Optional[int]
    optimum_ceiling: Optional[int]
    maximum_speed: Optional[int]
    optimum_speed: Optional[int]
    maximum_climb_rate: Optional[int]
