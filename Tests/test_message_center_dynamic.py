import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoAlertPresentException

class TestMessageCenter:
    # This is a utility/static method, not a pytest test case
    @staticmethod
    def run_message_center_tabs(driver):
        driver.get("https://www.entrata.com/products/message-center")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        
        # Click the Company News tab
        company_news = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='w-node-_3ac1575f-3fd3-6dc7-5b96-ca9b974269f8-974269f2']/a")))
        company_news.click()

        # Scroll to the footer
        footer = driver.find_element(By.TAG_NAME, "footer")
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(2)

        # Access and click all footer links, stop at 'sales@entrata.com'
        i = 0
        while True:
            footer = driver.find_element(By.TAG_NAME, "footer")
            footer_links = footer.find_elements(By.TAG_NAME, "a")
            if i >= len(footer_links):
                break
            link = footer_links[i]
            href = link.get_attribute("href")
            if href:
                print(f"Clicking footer link: {href}")
                driver.execute_script("arguments[0].click();", link)
                time.sleep(1)
                print(f"Visited: {driver.current_url}")
                # Try to close popup if it appears
                try:
                    close_btn = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'close') or contains(@class, 'close') or contains(text(), 'Close') or contains(text(), 'Cancel')]"))
                    )
                    close_btn.click()
                    print("Popup closed.")
                    time.sleep(1)
                except Exception:
                    print("No popup appeared or could not close popup.")
                # Try to handle JS alert if present
                try:
                    alert = driver.switch_to.alert
                    print(f"Alert text: {alert.text}")
                    alert.dismiss()
                    print("Alert accepted.")
                    time.sleep(1)
                except NoAlertPresentException:
                    print("No alert present.")
                driver.back()
                time.sleep(2)
                print(f"Returned to: {driver.current_url}")
                if 'sales@entrata.com' in href:
                    print("Reached sales@entrata.com, quitting browser.")
                    driver.quit()
                    return
                # Scroll back to footer after navigation if continuing
                i += 1
                continue
            i += 1

        # Example: Verify that clicking the 'Features' tab changes the visible content
        # feature_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Automated Communication')]")))
        # assert feature_heading.is_displayed()

        # # Example: Verify that clicking the 'Overview' tab changes the content back
        # overview_tab = driver.find_element(By.XPATH, "//button[contains(., 'Overview')]")
        # overview_tab.click()
        # overview_content = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Message Center') or contains(text(), 'Centralized communication')]")))
        # assert overview_content.is_displayed()
