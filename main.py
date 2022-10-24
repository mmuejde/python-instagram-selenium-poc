import time
import os
import requests
from requests import ConnectionError, Timeout
import logging
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

from utils import waiting_for

if not os.path.isdir('logs'):
    os.mkdir('logs')

logging.basicConfig(
    level=logging.DEBUG,
    filename=f'logs/{str(datetime.now())}.log',
    filemode='w',
    format='%(levelname)s - %(asctime)s - %(message)s'
)

URL = "http://www.instagram.com"
TIMEOUT = 5

USERNAME = "XXXXX"
PASSWORD = "XXXXX"

try:
    request = requests.get(URL, timeout=TIMEOUT)
    logging.info("Connected to the Internet")
except (ConnectionError, Timeout) as exception:
    logging.error("No internet connection!")
    exit()


browser = webdriver.Firefox()
browser.get(URL)

try:
    browser.find_element(By.XPATH, '//button[text()="Accept Al"]').click()
    logging.info('Popup button clicked')
except NoSuchElementException:
    logging.error("Popup button could not be located!", exc_info=True)
    browser.quit()

waiting_for(2)

try:
    username_field = browser.find_element(By.NAME, "username")
    username_field.send_keys(USERNAME)
except NoSuchElementException:
    logging.error("Username input could not be located!", exc_info=True)
    browser.quit()

try:
    password_field = browser.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD)
except NoSuchElementException:
    logging.error("Password input could not be located!", exc_info=True)
    browser.quit()

try:
    browser.find_element(
        By.XPATH, '//div[text()="Log In"]//parent::button').click()
    logging.info('Login button clicked')
except NoSuchElementException:
    logging.error("Login button could not be located!", exc_info=True)
    browser.quit()

waiting_for(5)

try:
    browser.find_element(By.XPATH, '//button[text()="Not Now"]').click()
    logging.info('Not Now button clicked')
except NoSuchElementException:
    logging.error("Not Now button could not be located!", exc_info=True)
    browser.quit()

waiting_for(5)

try:
    browser.find_element(By.XPATH, '//button[text()="Not Now"]').click()
    logging.info('Not Now button clicked')
except NoSuchElementException:
    logging.error("Not Now button could not be located!", exc_info=True)
    browser.quit()

waiting_for(5)
browser.quit()
