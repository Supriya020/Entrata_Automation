import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run in background
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_list_all_forms(driver):
    url = "https://www.entrata.com/"
    driver.get(url)

    forms = driver.find_elements(By.TAG_NAME, "form")
    print(f"Total forms found: {len(forms)}")

    for idx, form in enumerate(forms, start=1):
        print(f"\n--- Form #{idx} ---")
        print(f"Action: {form.get_attribute('action')}")
        print(f"Method: {form.get_attribute('method')}")
        inputs = form.find_elements(By.TAG_NAME, "input")
        for input_tag in inputs:
            print(f"Input name: {input_tag.get_attribute('name')} | Type: {input_tag.get_attribute('type')}")
