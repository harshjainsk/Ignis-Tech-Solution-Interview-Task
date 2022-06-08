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

