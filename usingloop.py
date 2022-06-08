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

    """
        Reject cookies functionality
        """
    clickon_cookie_rejection = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/footer/div[2]/div/div/div[2]/div/button[2]'))
    )
    clickon_cookie_rejection.click()
    # time.sleep(0.5)
    """Add a for loop before this to loop the rows from a csv

    """

    input_country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "react-select-2-input"))

    )
    input_country.click()

    # time.sleep(0.1)
    input_country.send_keys('India')
    time.sleep(1.8)
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
    # removing this sleep will hamper the program, hence don't remove time.sleep(3) below this line
    # time.sleep(3)
    # input_license.click()
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
    # time.sleep(1)

    # if natural gas:
    input_clickon_naturalgas = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[4]/div/div[2]/div[1]/div[1]/div/label'))
    )
    input_clickon_naturalgas.click()
    # time.sleep(1)

    # else:
    input_clickon_biomethane = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[4]/div/div[2]/div[1]/div[2]/div/label'))
    )
    input_clickon_biomethane.click()
    time.sleep(2.5)

    # payment functionality

    """
    Annual payment functionality
    """
    clickon_annual_payment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="root"]/div/form/div/div[1]/div/fieldset/div/div/div/div[1]/div/div/label/div'))
    )
    clickon_annual_payment.click()
    time.sleep(1)

    """ 
    30-day payment functionality
    """
    clickon_30day_payment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/fieldset/div/div/div/div[2]/div/div/label/div'))
    )
    clickon_30day_payment.click()
    time.sleep(1)

    """
    10-days payment functionality
    """
    clickon_10day_payment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/fieldset/div/div/div/div[3]/div/div/label/div'))
    )
    clickon_10day_payment.click()
    time.sleep(1)

    """
    New batch functionality
    """

    clickon_add_new_batch = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[5]/button'))
    )
    clickon_add_new_batch.click()

    """
    Minimizing the previous batch
    """
    clickon_hide_previous_batch = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[1]/div[1]/div/button[2]/span/span[2]'))
    )
    clickon_hide_previous_batch.click()

# ----------------------------------------------------------------------------------------------------------------------

    for i in range(2,4):
        input_country = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, f"react-select-{i+1}-input"))

        )
        input_country.click()

        # time.sleep(0.1)
        input_country.send_keys('French')
        time.sleep(3)
        input_country.send_keys(Keys.RETURN)

        """
        date
        """
        input_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/div[2]/div[2]/div[1]/div/input'))
        )

        input_date.send_keys('30/5/2022')
        input_date.send_keys(Keys.RETURN)

        """
        Licence plate input
        """

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        input_license = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/div[3]/div/div/div[1]/input')))
        # removing this sleep will hamper the program, hence don't remove time.sleep(3) below this line
        # time.sleep(3)
        # input_license.click()
        input_license.send_keys('DSK21')
        input_license.send_keys(Keys.RETURN)

        """
            fuel
            """
        input_clickon = WebDriverWait(driver, 10,
                                      ignored_exceptions=[ElementNotVisibleException,
                                                          ElementNotSelectableException]).until(
            EC.presence_of_element_located((By.ID, f"{i-1}")))
        input_clickon.click()
        time.sleep(1)

        # if natural gas:
        input_clickon_naturalgas = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/div[4]/div/div[2]/div[1]/div[1]/div/label'
            ))
        )
        input_clickon_naturalgas.click()
        time.sleep(1)

        # else:
        input_clickon_biomethane = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/div[4]/div/div[2]/div[1]/div[2]/div/label'
                 ))
        )
        input_clickon_biomethane.click()
        time.sleep(1)

        """
            Annual payment functionality
            """
        clickon_annual_payment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'//*[@id="root"]/div/form/div/div[1]/div[{i}]/fieldset/div/div/div/div[1]/div/div/label/div'
                 ))
        )
        clickon_annual_payment.click()
        time.sleep(1)

        """ 
        30-day payment functionality
        """
        clickon_30day_payment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'//*[@id="root"]/div/form/div/div[1]/div[{i}]/fieldset/div/div/div/div[2]/div/div/label/div'
                 ))
        )
        clickon_30day_payment.click()
        time.sleep(1)

        """
        10-days payment functionality
        """
        clickon_10day_payment = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/fieldset/div/div/div/div[3]/div/div/label/div'
                 ))
        )
        clickon_10day_payment.click()
        time.sleep(1)





        """
        New batch functionality
        """

        clickon_add_new_batch = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/div[5]/button'))
        )
        clickon_add_new_batch.click()

        """
        Minimizing the previous batch
        """
        clickon_hide_previous_batch = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f'/html/body/main/div/div/div/div/div/div/form/div/div[1]/div[{i}]/div[1]/div/button[2]/span/span[2]'))
        )
        clickon_hide_previous_batch.click()

    time.sleep(30)

finally:
    driver.quit()

driver.quit()