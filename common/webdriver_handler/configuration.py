from selenium import webdriver
from os import environ as env


def get_chrome_web_driver(options):
    return webdriver.Chrome(env["CHROME_DRIVER"], chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')


def set_extension(options):
    options.add_argument('--disable-extensions')


def set_popup_blocker(options):
    options.add_argument('--disable-popup-blocking')
