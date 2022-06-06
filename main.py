from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch")
time.sleep(3)

try:

    """Add a for loop before this to loop the rows from a csv
        
    """
    input_country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "react-select-2-input"))
    )
    input_country.click()

    # time.sleep(3)
    input_country.send_keys('IN - Republic of India')
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
    input_license = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[3]/div/div/div[1]/input'))
    )
    input_license.click()
    input_license.send_keys('DSK21')
    time.sleep(5)
    input_license.send_keys(Keys.RETURN)

    """
    If vehicle is powered by natural gas or bio-methane we click on the further checkboxes
    """
    input_clickon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[4]/div/div/input'))
    )
    input_clickon.click()
    time.sleep(10)

    
finally:
    driver.quit()

driver.quit()
