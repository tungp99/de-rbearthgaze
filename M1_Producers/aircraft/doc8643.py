__all__ = ["AircraftParser", "scrape"]

from typing import List

import requests as http
from bs4 import BeautifulSoup
from libs.logging import Logging
from libs.models.aircraft import RawAircraft


class AircraftParser(Logging):
    def __init__(self, icao: str) -> None:
        super().__init__(f"{self.__class__.__name__}#{icao}")

        self._icao = icao

    @property
    def url(self):
        return f"https://doc8643.com/aircraft/{self._icao}"

    def __download(self) -> str:
        r = http.get(
            self.url,
            timeout=6000,
            headers={"User-Agent": "fuck off cloudFare. shit company"},
        )
        if r.status_code != 200:
            raise RuntimeError(r.text)

        return r.text

    def __download_img(self, path: str) -> bytes:
        r = http.get(
            f"https://doc8643.com/{path}",
            timeout=6000,
            headers={"User-Agent": "fuck off cloudFare. shit company"},
        )
        if r.status_code != 200:
            raise RuntimeError(r.text)

        return r.content

    def parse(self) -> RawAircraft:
        html = self.__download()
        soup = BeautifulSoup(html, "html.parser")

        result = RawAircraft()

        # START: parsing

        # First table
        el_metadata = soup.select("h1")
        result.icao = self._icao
        result.classification = el_metadata[1].get_text()
        result.category = el_metadata[2].get_text()

        # Second Table
        el_manufacturers = soup.select(".col-12")
        result.manufacturers = tuple(map(lambda x: x.get_text(), el_manufacturers))

        # Third Table
        el_tech_details = soup.select(".col-2")
        result.wing_span = el_tech_details[0].get_text()
        result.length = el_tech_details[1].get_text()
        result.height = el_tech_details[2].get_text()
        result.mtow = el_tech_details[3].get_text()
        result.fuel_capacity = el_tech_details[4].get_text()
        result.maximum_range = el_tech_details[5].get_text()
        result.persons_on_board = el_tech_details[6].get_text()
        result.take_off_distance = el_tech_details[7].get_text()
        result.landing_distance = el_tech_details[8].get_text()
        result.absolute_ceiling = el_tech_details[9].get_text()
        result.optimum_ceiling = el_tech_details[10].get_text()
        result.maximum_speed = el_tech_details[11].get_text()
        result.optimum_speed = el_tech_details[12].get_text()
        result.maximum_climb_rate = el_tech_details[13].get_text()

        # Img
        result.img_3d = soup.select(".views_img img")[0]["src"]
        # data = self.__download_img(result.img_3d)
        # with open(
        #     f"assets/aircrafts_img/{self._icao}_3D.{result.img_3d.split('.')[-1]}", "wb"
        # ) as f:
        #     f.write(data)

        result.img_cs = soup.select(".views_img img")[1]["src"]
        # data = self.__download_img(result.img_cs)
        # with open(
        #     f"assets/aircrafts_img/{self._icao}_CS.{result.img_cs.split('.')[-1]}", "wb"
        # ) as f:
        #     f.write(data)

        # END: parsing

        self.logger.debug(result)
        return result


def scrape(icao_list: List[str]):
    for icao in icao_list:
        parser = AircraftParser(icao)
        yield parser.parse()
