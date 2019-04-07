# -*- coding: utf-8 -*-
"""
Scrape 3D models from McMaster-Carr.
Requirements: Chromedriver.exe is in the same folder as this script.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
TEST_PART_NUMBERS = ['98173A200', '7529K105', '93250A440']

def fetch_model(part_numbers, delay=3):
    """Fetch 3D models from McMaster Carr

    Arguments:
        part_numbers {string} -- McMaster Carr Part Number

    Keyword Arguments:
        delay {int} -- Time delay in seconds to pause for the web page to load (default: {3})
    """
    if isinstance(part_numbers) is str:
        part_numbers = [part_numbers]
    #Start browser
    options = Options()
    options.headless = True
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    #For each part number
    for part_number in part_numbers:
        driver.get('https://www.mcmaster.com/#' + str(part_number) + '/')
        #Pause for page to load
        time.sleep(delay)
        #Find and Click submit button
        try:
            try:
                submit_button = driver.find_element_by_class_name("button-save--sidebyside")
            except exceptions.NoSuchElementException:
                submit_button = driver.find_element_by_class_name("button-save--stacked")
            finally:
                submit_button.click()
        except exceptions.WebDriverException:
            print('No button found or other error occured')
        finally:
            time.sleep(delay)

    driver.close()

fetch_model(TEST_PART_NUMBERS)
