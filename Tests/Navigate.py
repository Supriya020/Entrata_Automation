import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

driver = webdriver.Chrome()
driver.get("https://www.entrata.com")

driver.maximize_window()
time.sleep(10)
    # Handle cookie banner
try:
    cookie = wait.until(EC.element_to_be_clickable((By.ID, "69bec5c9-7193-4426-8401-518857753121")))
    cookie.click()
    print("🍪 Cookie banner dismissed.")
except TimeoutException:
    print("No cookie banner found.")