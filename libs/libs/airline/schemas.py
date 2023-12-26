import json

from libs.core import SingletonMeta
from libs.kafka.schema import AbstractSchemaRegistry


class AirlineSchemaRegistry(AbstractSchemaRegistry, metaclass=SingletonMeta):
    @property
    def raw_schema(self):
        return json.dumps(
            {
                "type": "record",
                "name": "Airline",
                "namespace": "neot.de.rbearthgaze",
                "doc": "Typical Airline message according to https://openflights.org/data.php#airline.",
                "fields": [
                    {
                        "name": "id",
                        "type": ["string", "null"],
                        "doc": "Unique OpenFlights identifier for this airline.",
                    },
                    {"name": "name", "type": ["string", "null"], "doc": "Name of the airline."},
                    {
                        "name": "alias",
                        "type": ["string", "null"],
                        "doc": "Alias of the airline. For example, All Nippon Airways is commonly known as \u0027ANA\u0027.",
                    },
                    {
                        "name": "iata",
                        "type": ["string", "null"],
                        "doc": "2-letter IATA code, if available.",
                    },
                    {
                        "name": "icao",
                        "type": ["string", "null"],
                        "doc": "3-letter ICAO code, if available.",
                    },
                    {"name": "callsign", "type": ["string", "null"], "doc": "Airline callsign."},
                    {
                        "name": "country",
                        "type": ["string", "null"],
                        "doc": "Country or territory where airport is located. See Countries to cross-reference to ISO 3166-1 codes.",
                    },
                    {
                        "name": "active",
                        "type": [{"type": "enum", "name": "Active", "symbols": ["Y", "N"]}, "null"],
                        "doc": "\u0027Y\u0027 if the airline is or has until recently been operational, \u0027N\u0027 if it is defunct. This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as \u0027Y\u0027.",
                    },
                ],
            }
        )
