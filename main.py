from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch")
driver.implicitly_wait(10)
time.sleep(3)

try:

    """Add a for loop before this to loop the rows from a csv
        
    """
    input_country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "react-select-2-input"))
    )
    input_country.click()

    time.sleep(3)
    input_country.send_keys('India')
    # time.sleep(5)
    input_country.send_keys(Keys.RETURN)

    """
    Date is being taken as input and then sent to the web page
    """
    input_date = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div/input'))
    )

    # input_date.click()

    input_date.send_keys('30/5/2022')
    input_date.send_keys(Keys.RETURN)

    """
    License value is being taken as input and then sent to the web page
    """
    # input_license = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '//*[@id="root"]/div/form/div/div[1]/div[2]/div[3]/div/div/div[1]'))
    # )
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    input_license = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[3]/div/div/div[1]/input")))
    input_license.click()
    input_license.send_keys('DSK21')
    input_license.send_keys(Keys.RETURN)
    # time.sleep(3)

    """
    If vehicle is powered by natural gas or bio-methane we click on the further checkboxes
    """

    """ This should go in a if statement when the value of
        `powered by` = 'natural gas' or 'biomethane' 
    """

    # if df['Powered by'] is 'Nan':

    input_clickon = WebDriverWait(driver, 10,
                                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]).until(
        EC.presence_of_element_located((By.ID, "0")))
    input_clickon.click()
    time.sleep(5)

    # if natural gas:
    # input_clickon_naturalgas = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID,
    #          'natural_gas_radio_array_option_1'))
    # )
    # input_clickon_naturalgas.click()
    #
    # time.sleep(5)

    # else:
    # input_clickon_biomethane = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID,
    #          'bio_methane_radio_array_option_1'))
    # )
    # input_clickon_biomethane.click()
    #
    # time.sleep(10)


finally:
    driver.quit()

driver.quit()
