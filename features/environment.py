import os
import shutil
import subprocess
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities import ConfigReader

url = ConfigReader.read_configuration("Basic Information", "url")
browser = ConfigReader.read_configuration("Basic Information", "browser")
ALLURE_REPORT_DIR = 'allure_reports'

def clean_allure_reports():
    """Cleans up the allure reports directory before each test run."""
    if os.path.exists(ALLURE_REPORT_DIR):
        shutil.rmtree(ALLURE_REPORT_DIR)
    os.makedirs(ALLURE_REPORT_DIR)

def before_scenario(context, scenario):
    """Sets up the browser before each test scenario."""
    clean_allure_reports()

    if browser == 'chrome':
        chrome_install = ChromeDriverManager().install()
        folder = os.path.dirname(chrome_install)
        chromedriver_path = os.path.join(folder, "chromedriver.exe")
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(chromedriver_path)
        context.driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=options)
    elif browser == 'edge':
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = EdgeService(EdgeChromiumDriverManager().install())
        context.driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Browser '{browser}' is not supported")

    context.driver.get(url)

@allure.step
def take_screenshot(context, step_name):
    """Takes a screenshot during test steps."""
    allure.attach(context.driver.get_screenshot_as_png(), name=step_name, attachment_type=allure.attachment_type.PNG)

def after_step(context, step):
    """Logs information and takes screenshots after each step."""
    take_screenshot(context, step.name)
    if step.status == "failed":
        with allure.step(f"Error in step: {step.name}"):
            allure.attach(step.exception, name="Error Message", attachment_type=allure.attachment_type.TEXT)

def after_all(context):
    """Serves and opens the Allure report after the test execution."""
    subprocess.run(f"allure serve {ALLURE_REPORT_DIR}", shell=True)

