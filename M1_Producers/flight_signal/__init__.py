import logging
from collections import defaultdict

from libs.configuration import configure
from libs.kafka import MessageProducer
from libs.models.flight_signal import RawFlightSignal
from ogn.client import AprsClient
from ogn.parser import ParseError, parse_aprs, parse_comment

__MODULE = "M1_Producers.flight"
logger = logging.getLogger(__MODULE)


def run():
    config = configure()
    p = MessageProducer[RawFlightSignal](config.kafka.flight_raw_topic)

    def process(beacon: str):
        try:
            parsed = defaultdict(lambda: None)
            parsed.update(parse_aprs(beacon))
            parsed.update(parse_comment(parsed["comment"]))

            if parsed["beacon_type"] == "aprs_aircraft":
                logger.info(beacon)

                parsed.pop("raw_message")
                parsed.pop("comment")
                parsed.pop("no-tracking")
                parsed.pop("stealth")
                parsed.pop("relay")

                if parsed["gps_quality"] is not None:
                    parsed["gps_quality_vertical"] = parsed["gps_quality"]["vertical"]
                    parsed["gps_quality_horizontal"] = parsed["gps_quality"]["horizontal"]
                    parsed.pop("gps_quality")

                data = RawFlightSignal(**parsed)
                p.produce(data)
        except ParseError as e:
            logger.error(e)
        except NotImplementedError as e:
            logger.error(f"{e}: {beacon}")

    client = AprsClient("N0CALL")
    client.connect()

    try:
        client.run(callback=process, autoreconnect=True)
    except KeyboardInterrupt:
        logger.info("Stop ogn gateway")
        client.disconnect()
