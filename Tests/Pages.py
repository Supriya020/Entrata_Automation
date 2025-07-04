import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        sign_button = self.driver.find_element(By.XPATH, "//a[@class='button is-secondary is-nav w-button']")
        sign_button.click()

    def click_property_login(self):
        prop_login = self.driver.find_element(By.XPATH, "//a[@class='button w-inline-block']")
        prop_login.click()

    def click_resident_login(self):
        res_login = self.driver.find_element(By.XPATH, "//a[@class='button w-variant-a4bcaccf-a627-9db9-f960-605351be4d34 w-inline-block']")
        res_login.click()

    def click_watch_demo(self):
        watch_demo = self.driver.find_element(By.XPATH, "//a[normalize-space()='Watch demo']")
        watch_demo.click()

    def go_home(self):
        try:
            logo = self.driver.find_element(By.XPATH, "//a[@class='navbar-brand w-nav-brand']")
            logo.click()
            time.sleep(2)
        except Exception:
            self.driver.get("https://www.entrata.com")
            time.sleep(2)


class DemoPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_demo_form(self, first, last, email, phone, company, title, unit_count, i_am):
        self.driver.find_element(By.ID, "FirstName").send_keys(first)
        self.driver.find_element(By.ID, "LastName").send_keys(last)
        self.driver.find_element(By.ID, "Email").send_keys(email)
        self.driver.find_element(By.ID, "Phone").send_keys(phone)
        self.driver.find_element(By.ID, "Company").send_keys(company)
        self.driver.find_element(By.ID, "Title").send_keys(title)
        total_unit = self.driver.find_element(By.NAME, "Unit_Count__c")
        Select(total_unit).select_by_value(unit_count)
        i_am_elem = self.driver.find_element(By.NAME, "demoRequest")
        Select(i_am_elem).select_by_value(i_am)


class FormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def open_products(self):
        product = self.driver.find_element(By.XPATH, "//div[contains(text(),'Products')]")
        self.actions.move_to_element(product).perform()
        time.sleep(2)

    def click_digital_marketing(self):
        digital_marketing = self.driver.find_element(By.XPATH, "//div[normalize-space()='Digital Marketing Bundle']")
        digital_marketing.click()
        time.sleep(2)

    def ai_application(self):
        ai_application = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='AI & Automation']"))
        )
        self.actions.move_to_element(ai_application).click().perform()
        time.sleep(2)
        eli = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='ELI+']"))
        )
        eli.click()
        time.sleep(2)


    def open_solutions(self):
        solutions = self.driver.find_element(By.ID, "w-dropdown-toggle-1")
        self.actions.move_to_element(solutions).perform()
        time.sleep(2)

    def click_student(self):
        student = self.driver.find_element(By.XPATH, "//div[normalize-space()='Student']")
        student.click()
        time.sleep(2)

    def open_resources(self):
        resources = self.driver.find_element(By.ID, "w-dropdown-toggle-2")
        self.actions.move_to_element(resources).perform()
        time.sleep(2)

    def click_blog(self):
        blog = self.driver.find_element(By.XPATH, "//div[normalize-space()='Blog']")
        blog.click()
        time.sleep(2)
