import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Pages import MainPage, DemoPage, FormsPage
from test_message_center_dynamic import TestMessageCenter

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.entrata.com")
    driver.maximize_window()
    WebDriverWait(driver, 10)
    time.sleep(5)
    yield driver
    driver.quit()

#This testcase will open all the forms one by one.
#added assertions to verify the presence of elements and functionality.
@pytest.mark.form
def test_pages_flow(driver):
    main = MainPage(driver)
    demo = DemoPage(driver)

    # Sign In and Property Login
    main.click_sign_in()
    # Assert that the sign-in page loaded (URL or element)
    assert "sign-in" in driver.current_url, f"Expected 'sign-in' in URL, got {driver.current_url}"
    main.click_property_login()
    driver.back()

    # Resident Login
    main.click_resident_login()
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "email")))
    # Assert that the email field is present
    email_field = driver.find_element(By.NAME, "email")
    assert email_field.is_displayed(), "Email field not visible on Resident Login"
    email_field.send_keys("suprizangru@gmail.com")
    password_field = driver.find_element(By.NAME, "password")
    assert password_field.is_displayed(), "Password field not visible on Resident Login"
    password_field.send_keys("@fantasticmo0d")
    time.sleep(5)  # Wait for 5 seconds to observe the result before closing the browser
    

    # Watch Demo
    main.go_home()
    main.click_watch_demo()
    # Assert that demo form is present
    assert driver.find_element(By.ID, "FirstName").is_displayed(), "Demo form not loaded"
    demo.fill_demo_form(
        first="Supri",
        last="Zangruche",
        email="suprizangru@gmail.com",
        phone="8197705992",
        company="BHEL",
        title="Engineer",
        unit_count="101 - 300",
        i_am="a Resident"
    )
    main.go_home()

#This testcase will open all the pages one by one.
@pytest.mark.page
def test_forms_flow(driver):
    main = MainPage(driver)
    forms = FormsPage(driver)
    forms.open_products()

    # Assert that Products menu is open (check for a visible submenu or element)
    assert driver.find_element(By.XPATH, "//div[contains(text(),'Products')]").is_displayed(), "Products menu not visible"
    forms.click_digital_marketing()

    # Assert navigation to Digital Marketing page (check URL or heading)
    assert "digital-marketing" in driver.current_url or driver.find_elements(By.XPATH, "//div[normalize-space()='Digital Marketing Bundle']"), "Did not navigate to Digital Marketing Bundle"

    main.go_home()
    forms.open_products()
    forms.ai_application()

    # Navigate to ELI+ and then go back to the main page
    print(f"Navigated to: {driver.current_url}")
    if "ai.entrata.com" in driver.current_url:
        print("On ELI+ site.")
    else:
        print(f"Expected ai.entrata.com, got {driver.current_url}")
    if "Work differently with ELI+" in driver.page_source:
        print("ELI+ landing text found.")
    else:
        print("ELI+ landing text not found.")
    driver.back()  # Go back to the main Entrata page

    main.go_home()
    forms.open_solutions()

    # Print Solutions menu info
    if driver.find_element(By.ID, "w-dropdown-toggle-1").is_displayed():
        print("Solutions menu visible.")
    else:
        print("Solutions menu not visible.")
    forms.click_student()

    # Print Student section info
    if driver.find_element(By.XPATH, "//div[normalize-space()='Student']").is_displayed():
        print("Student section visible.")
    else:
        print("Student section not visible.")
    main.go_home()
    forms.open_resources()

    # Print Resources menu info
    if driver.find_element(By.ID, "w-dropdown-toggle-2").is_displayed():
        print("Resources menu visible.")
    else:
        print("Resources menu not visible.")
    forms.click_blog()

    # Print Blog section info
    if driver.find_element(By.XPATH, "//div[normalize-space()='Blog']").is_displayed():
        print("Blog section visible.")
    else:
        print("Blog section not visible.")
    main.go_home()

# This test case will open all the pages one by one.
# After clicking on one page, it will navigate back and click the next page.
@pytest.mark.dynamic
def test_message_center(driver):
    TestMessageCenter.run_message_center_tabs(driver)

