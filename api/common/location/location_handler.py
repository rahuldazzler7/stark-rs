from selenium import webdriver
import webbrowser
import requests
from os import environ as env
from time import sleep
from api.common.webdriver_handler.configuration import (get_web_driver_options,
                                                    get_chrome_web_driver,
                                                    set_ignore_certificate_error,
                                                    set_browser_as_incognito,
                                                    set_automation_as_head_less,
                                                    set_extension,
                                                    set_popup_blocker)


class Location_details:
    def __init__(self):
        options = get_web_driver_options()
        set_automation_as_head_less(options)
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        set_extension(options)
        set_popup_blocker(options)
        self.driver = get_chrome_web_driver(options)

    def get_my_coordinates(self) -> dict:
        self.driver.get("https://www.google.co.in/maps/search/where+am+I")
        sleep(6)
        url = self.driver.current_url
        url = url.split("/")
        url = url[6][1:]
        url = url.split(",")
        self.driver.close()
        return {"latitude": url[0], "longitude": url[1]}


def find_nearest_locations(query: str) -> bool:
    query = query.replace(" ", "+")
    lc = Location_details()
    coordinates = lc.get_my_coordinates()
    webbrowser.get(f"{env['BROWSER_PATH']} %s").open(f"https://www.google.co.in/maps/search/"
                                                     f"{query}/@{coordinates['latitude'], coordinates['longitude']}")
    return {"status": True, "message": "Here are the list of your findings"}


def get_place(lat: str, lng: str) -> dict:
    try:
        api_url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lng}&key={env['OPENCAGE_ACCESS_KEY']}"
        location_details = requests.get(api_url)
        details = location_details.json()
        return {"details": details, "place": details['results'][0]['formatted']}
    except Exception as err:
        return {"Error": f"{err}"}
