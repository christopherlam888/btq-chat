from .site import *

from .selenium_options import *

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import itertools
import threading
import time
import sys

done = True


def animate_loading():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write(f"\r {c} ")
        sys.stdout.flush()
        time.sleep(0.1)


def get_element(xpath):
    try:
        return driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None


def scrape(prompt):
    global done
    done = False
    t = threading.Thread(target=animate_loading)
    t.daemon = True
    t.start()
    driver.implicitly_wait(10)
    driver.get(site)
    if get_element(".//button[@class=' css-47sehv']"):
        driver.find_element(By.XPATH, ".//button[@class=' css-47sehv']").click()
    driver.find_element(By.TAG_NAME, "textarea").send_keys(prompt)
    driver.find_element(By.TAG_NAME, "textarea").send_keys(Keys.ENTER)
    while get_element(".//div[@class='mwai-timer']"):
        time.sleep(0.1)
    response = driver.find_elements(By.XPATH, ".//span[@class='mwai-text']")[2].text
    driver.quit()
    done = True
    return response
