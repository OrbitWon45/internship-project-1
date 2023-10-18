from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logging import logger

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

# Google Chrome

    service = Service(executable_path=r'C:\Users\white\Downloads\internship-project\internship-project-1\chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)

# Fire Fox

    # service = Service(executable_path=r'C:\Users\white\Downloads\internship-project\internship-project-1\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    # Headless

    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    # service = Service(executable_path=r'C:\Users\white\Downloads\internship-project\internship-project-1\chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options = options,
    #     service=service
    # )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
