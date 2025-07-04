Entrata Selenium Test Automation Suite
========================================

This project contains automated UI tests for the Entrata website using Selenium WebDriver and pytest, following the Page Object Model (POM) design pattern.

Project Structure:
------------------
Entrata/
│
├── main.py
├── README.txt
├── requirements.txt
├── pytest.ini
├── .gitignore
├── Tests/
│   ├── Pages.py
│   ├── Navigate.py
│   ├── test_forms.py
│   ├── test_message_center_dynamic.py
│   └── __pycache__/
├── venv/
├── __pycache__/
└── .pytest_cache/

How to Run Tests:
-----------------
1. **Activate your Python virtual environment:**
   - Windows: `venv\Scripts\activate`

2. **Install dependencies:**
   - `pip install -r requirements.txt`

3. **Run all test cases:**
   - `pytest -v`

4. **Run tests with a specific marker (e.g., only form tests):**
   - pytest -v -m form
   - pytest -v -m page
   - pytest -v -m dynamic

5. **Generate Allure results:**
   - `pytest --alluredir=allure-results`
   - Then generate and view the report:
     - `allure serve allure-results`

6. **Generate an HTML report:**
   - `pytest --html=report.html`

How to Push Changes to Your Repository:
--------------------------------------
1. Check the status of your changes:
   - `git status`
2. Add the files you want to commit:
   - `git add .`  (to add all changes)
3. Commit your changes with a message:
   - `git commit -m "Describe your changes here"`
4. Push your changes to the remote repository:
   - `git push origin main`  (replace `main` with your branch name if different)


